# Reference: https://github.com/kwea123/CasMVSNet_pl
#            https://github.com/zju3dv/LoFTR

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init
from einops import reduce, rearrange, repeat
from .modules import *
import copy
import math


class PositionEncodingSine(nn.Module):
    """
    This is a sinusoidal position encoding that generalized to 2-dimensional images
    """

    def __init__(self, d_model, max_shape=(256, 256), temp_bug_fix=True):
        """
        Args:
            max_shape (tuple): for 1/8 featmap, the max length of 256 corresponds to 2048 pixels
            temp_bug_fix (bool): As noted in this [issue](https://github.com/zju3dv/LoFTR/issues/41),
                the original implementation of LoFTR includes a bug in the pos-enc impl, which has little impact
                on the final performance. For now, we keep both impls for backward compatability.
                We will remove the buggy impl after re-training all variants of our released models.
        """
        super().__init__()

        pe = torch.zeros((d_model, *max_shape))
        y_position = torch.ones(max_shape).cumsum(0).float().unsqueeze(0)
        x_position = torch.ones(max_shape).cumsum(1).float().unsqueeze(0)
        if temp_bug_fix:
            div_term = torch.exp(torch.arange(0, d_model // 2, 2).float() * (-math.log(10000.0) / (d_model // 2)))
        else:  # a buggy implementation (for backward compatability only)
            div_term = torch.exp(torch.arange(0, d_model // 2, 2).float() * (-math.log(10000.0) / d_model // 2))
        div_term = div_term[:, None, None]  # [C//4, 1, 1]
        pe[0::4, :, :] = torch.sin(x_position * div_term)
        pe[1::4, :, :] = torch.cos(x_position * div_term)
        pe[2::4, :, :] = torch.sin(y_position * div_term)
        pe[3::4, :, :] = torch.cos(y_position * div_term)

        self.register_buffer('pe', pe.unsqueeze(0), persistent=False)  # [1, C, H, W]

    def forward(self, x):
        """
        Args:
            x: [N=B*V, C, H, W]
        """
        return x + self.pe[:, :, :x.size(2), :x.size(3)]


class AttentionLayer(nn.Module):
    def __init__(self, d_model, nhead):
        super(AttentionLayer, self).__init__()

        self.dim = d_model // nhead
        self.nhead = nhead

        # multi-head attention
        self.q_proj = nn.Linear(d_model, d_model, bias=False)
        self.k_proj = nn.Linear(d_model, d_model, bias=False)
        self.v_proj = nn.Linear(d_model, d_model, bias=False)
        self.attention = LinearAttention()
        self.merge = nn.Linear(d_model, d_model, bias=False)

        # feed-forward network
        self.mlp = nn.Sequential(
            nn.Linear(d_model * 2, d_model * 2, bias=False),
            nn.ReLU(True),
            nn.Linear(d_model * 2, d_model, bias=False),
        )

        # norm and dropout
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)

    def forward(self, x, source, x_mask=None, source_mask=None):
        """
        Args:
            x (torch.Tensor): [N, L, C]
            source (torch.Tensor): [N, S, C]
            x_mask (torch.Tensor): [N, L] (optional)
            source_mask (torch.Tensor): [N, S] (optional)
        """
        bs = x.shape[0]
        query, key, value = x, source, source

        # multi-head attention
        query = self.q_proj(query).view(bs, -1, self.nhead, self.dim)  # [N, L, (H, D)]
        key = self.k_proj(key).view(bs, -1, self.nhead, self.dim)  # [N, S, (H, D)]
        value = self.v_proj(value).view(bs, -1, self.nhead, self.dim)
        message = self.attention(query, key, value, q_mask=x_mask, kv_mask=source_mask)  # [N, L, (H, D)]
        message = self.merge(message.view(bs, -1, self.nhead * self.dim))  # [N, L, C]
        message = self.norm1(message)

        # feed-forward network
        message = self.mlp(torch.cat([x, message], dim=2))
        message = self.norm2(message)

        return x + message


class FeatureMatchingTransformer(nn.Module):
    """Feature Matching Transformer (FMT) module."""

    def __init__(self, d_model=32, nhead=1):
        super(FeatureMatchingTransformer, self).__init__()

        self.d_model = d_model
        self.nhead = nhead
        self.layer_names = ['self', 'cross'] * 2
        encoder_layer = AttentionLayer(d_model, nhead)
        self.layers = nn.ModuleList([copy.deepcopy(encoder_layer) for _ in range(len(self.layer_names))])
        self._reset_parameters()

    def _reset_parameters(self):
        for p in self.parameters():
            if p.dim() > 1:
                nn.init.xavier_uniform_(p)

    def forward(self, feats, B, V, mask0=None, mask1=None):
        """
        Args:
            feats (torch.Tensor): [N=B*V, C, H, W]
            mask0 (torch.Tensor): [N, L] (optional)
            mask1 (torch.Tensor): [N, S] (optional)
        """

        assert self.d_model == feats.shape[1], "the feature number of src and transformer must be equal"
        N, C, H, W = feats.shape
        feats = feats.reshape(B, V, C, H, W)
        feats = rearrange(feats, 'b v c h w -> v b (h w) c')
        for layer, name in zip(self.layers, self.layer_names):
            if name == 'self':
                feats[0] = layer(feats[0], feats[0], mask0, mask0)
                for index in range(1, feats.shape[0]):
                    feats[index] = layer(feats[index], feats[index], mask1, mask1)
            elif name == 'cross':
                # feat0 = layer(feat0, feat1, mask0, mask1)
                for index in range(1, feats.shape[0]):
                    feats[index] = layer(feats[index], feats[0], mask1, mask0)

        feats = feats.reshape(B * V, C, H, W)
        return feats


class FeatureNet(nn.Module):
    """
    output 3 levels of features using a FPN structure
    """

    def __init__(self):
        super(FeatureNet, self).__init__()

        self.conv0 = nn.Sequential(
            ConvBnReLU(3, 8, 3, 1, 1),
            ConvBnReLU(8, 8, 3, 1, 1)
        )

        self.conv1 = nn.Sequential(
            ConvBnReLU(8, 16, 5, 2, 2),
            ConvBnReLU(16, 16, 3, 1, 1),
            ConvBnReLU(16, 16, 3, 1, 1)
        )

        self.conv2 = nn.Sequential(
            ConvBnReLU(16, 32, 5, 2, 2),
            ConvBnReLU(32, 32, 3, 1, 1),
            ConvBnReLU(32, 32, 3, 1, 1)
        )

        self.toplayer = nn.Conv2d(32, 32, 1)
        self.lat1 = nn.Conv2d(16, 32, 1)
        self.lat0 = nn.Conv2d(8, 32, 1)

        # to reduce channel size of the outputs from FPN
        self.smooth1 = nn.Conv2d(32, 16, 3, padding=1)
        self.smooth0 = nn.Conv2d(32, 8, 3, padding=1)

        # self.arf0 = deformconvgnrelu(8, 8, kernel_size=3, stride=1, dilation=1)
        # self.arf1 = deformconvgnrelu(16, 16, kernel_size=3, stride=1, dilation=1)
        self.arf2 = deformconvgnrelu(32, 32, kernel_size=3, stride=1, dilation=1)

        self.pos_encoding = PositionEncodingSine(d_model=32, temp_bug_fix=True)
        self.fmt = FeatureMatchingTransformer(d_model=32, nhead=1)

    def _upsample_add(self, x, y):
        return F.interpolate(x, scale_factor=2, mode="bilinear", align_corners=True) + y

    def forward(self, x, B, V):
        # x: (B, 3, H, W)
        conv0 = self.conv0(x)  # (B, 8, H, W)
        conv1 = self.conv1(conv0)  # (B, 16, H//2, W//2)
        conv2 = self.conv2(conv1)  # (B, 32, H//4, W//4)
        feat2 = self.toplayer(conv2)  # (B, 32, H//4, W//4)
        feat1 = self._upsample_add(feat2, self.lat1(conv1))  # (B, 32, H//2, W//2)
        feat0 = self._upsample_add(feat1, self.lat0(conv0))  # (B, 32, H, W)

        feat2 = self.arf2(feat2)  # (B, 32, H//4, W//4)
        # feat1 = self.arf1(feat1)  # (B, 16, H//2, W//2)
        # feat0 = self.arf0(feat0)  # (B, 8, H, W)

        feat2 = self.pos_encoding(feat2)  # (B, 32, H//4, W//4)
        feat2 = self.fmt(feat2, B, V)  # (B, 32, H//4, W//4)

        feat1 = feat1 + F.interpolate(feat2, scale_factor=2, mode='bilinear', align_corners=True)  # (B, 32, H//2, W//2)
        feat0 = feat0 + F.interpolate(feat2, scale_factor=4, mode='bilinear', align_corners=True)  # (B, 32, H, W)

        # reduce output channels
        feat1 = self.smooth1(feat1)  # (B, 16, H//2, W//2)
        feat0 = self.smooth0(feat0)  # (B, 8, H, W)

        feats = {"level_0": feat0, "level_1": feat1, "level_2": feat2}

        return feats


class CostRegNet(nn.Module):
    def __init__(self, in_channels):
        super(CostRegNet, self).__init__()
        self.conv0 = ConvBnReLU3D(in_channels, 8)

        self.conv1 = ConvBnReLU3D(8, 16, stride=2)
        self.conv2 = ConvBnReLU3D(16, 16)

        self.conv3 = ConvBnReLU3D(16, 32, stride=2)
        self.conv4 = ConvBnReLU3D(32, 32)

        self.conv5 = ConvBnReLU3D(32, 64, stride=2)
        self.conv6 = ConvBnReLU3D(64, 64)

        self.conv7 = nn.Sequential(
            nn.ConvTranspose3d(64, 32, 3, padding=1, output_padding=1, stride=2, bias=False),
            nn.BatchNorm3d(32),
            nn.ReLU()
        )

        self.conv9 = nn.Sequential(
            nn.ConvTranspose3d(32, 16, 3, padding=1, output_padding=1, stride=2, bias=False),
            nn.BatchNorm3d(16),
            nn.ReLU()
        )

        self.conv11 = nn.Sequential(
            nn.ConvTranspose3d(16, 8, 3, padding=1, output_padding=1, stride=2, bias=False),
            nn.BatchNorm3d(8),
            nn.ReLU()
        )

        self.prob = nn.Conv3d(8, 1, 3, stride=1, padding=1)

    def forward(self, x):
        conv0 = self.conv0(x)
        conv2 = self.conv2(self.conv1(conv0))
        conv4 = self.conv4(self.conv3(conv2))

        x = self.conv6(self.conv5(conv4))
        x = conv4 + self.conv7(x)
        del conv4
        x = conv2 + self.conv9(x)
        del conv2
        x = conv0 + self.conv11(x)
        del conv0
        x = self.prob(x)
        return x


class CascadeMVSNet(nn.Module):
    def __init__(self, n_depths=[8, 32, 48], interval_ratios=[1, 2, 4], num_groups=4):
        super(CascadeMVSNet, self).__init__()
        self.levels = 3  # 3 depth levels
        self.n_depths = n_depths
        self.interval_ratios = interval_ratios
        self.G = num_groups  # number of groups in groupwise correlation
        self.feature = FeatureNet()
        for l in range(self.levels):
            if self.G > 1:
                cost_reg_l = CostRegNet(self.G)
            else:
                cost_reg_l = CostRegNet(8 * 2 ** l)
            setattr(self, f'cost_reg_{l}', cost_reg_l)

    def predict_depth(self, feats, proj_mats, depth_values, cost_reg):
        # feats: (B, V, C, H, W)
        # proj_mats: (B, V-1, 3, 4)
        # depth_values: (B, D, H, W)
        # cost_reg: nn.Module of input (B, C, D, h, w) and output (B, 1, D, h, w)
        B, V, C, H, W = feats.shape
        D = depth_values.shape[1]

        ref_feats, src_feats = feats[:, 0], feats[:, 1:]
        src_feats = rearrange(src_feats, 'b vm1 c h w -> vm1 b c h w')  # (V-1, B, C, h, w)
        proj_mats = rearrange(proj_mats, 'b vm1 x y -> vm1 b x y')  # (V-1, B, 3, 4)

        ref_volume = rearrange(ref_feats, 'b c h w -> b c 1 h w')
        ref_volume = repeat(ref_volume, 'b c 1 h w -> b c d h w', d=D)  # (B, C, D, h, w)
        if self.G == 1:
            volume_sum = ref_volume
            volume_sq_sum = ref_volume ** 2
        else:
            ref_volume = ref_volume.view(B, self.G, C // self.G, *ref_volume.shape[-3:])
            volume_sum = 0
        del ref_feats

        for src_feat, proj_mat in zip(src_feats, proj_mats):
            warped_volume = homo_warp(src_feat, proj_mat, depth_values)
            warped_volume = warped_volume.to(ref_volume.dtype)
            if self.G == 1:
                if self.training:
                    volume_sum = volume_sum + warped_volume
                    volume_sq_sum = volume_sq_sum + warped_volume ** 2
                else:
                    volume_sum += warped_volume
                    volume_sq_sum += warped_volume.pow_(2)
            else:
                warped_volume = warped_volume.view_as(ref_volume)
                if self.training:
                    volume_sum = volume_sum + warped_volume  # (B, G, C//G, D, h, w)
                else:
                    volume_sum += warped_volume
            del warped_volume, src_feat, proj_mat
        del src_feats, proj_mats
        # aggregate multiple feature volumes by variance
        if self.G == 1:
            volume_variance = volume_sq_sum.div_(V).sub_(volume_sum.div_(V).pow_(2))
            del volume_sq_sum, volume_sum
        else:
            volume_variance = reduce(volume_sum * ref_volume, 'b g c d h w -> b g d h w', 'mean').div_(
                V - 1)  # (B, G, D, h, w)
            del volume_sum, ref_volume

        cost_reg = rearrange(cost_reg(volume_variance), 'b 1 d h w -> b d h w')
        prob_volume = F.softmax(cost_reg, 1)  # (B, D, h, w)
        del cost_reg
        depth = depth_regression(prob_volume, depth_values)

        with torch.no_grad():
            # sum probability of 4 consecutive depth indices
            prob_volume_sum4 = 4 * F.avg_pool3d(F.pad(prob_volume.unsqueeze(1), pad=(0, 0, 0, 0, 1, 2)), (4, 1, 1),
                                                stride=1).squeeze(1)  # (B, D, h, w)

            # find the (rounded) index that is the final prediction
            depth_index = depth_regression(prob_volume, torch.arange(D, device=prob_volume.device,
                                                                     dtype=prob_volume.dtype)).long()  # (B, h, w)

            depth_index = torch.clamp(depth_index, 0, D - 1)
            # the confidence is the 4-sum probability at this index
            confidence = torch.gather(prob_volume_sum4, 1, depth_index.unsqueeze(1)).squeeze(1)  # (B, h, w)

        return depth, confidence

    def forward(self, imgs, proj_mats, init_depth_min, depth_interval):
        # imgs: (B, V, 3, H, W)
        # proj_mats: (B, V-1, self.levels, 3, 4) from fine to coarse
        # init_depth_min, depth_interval: (B) or float
        B, V, _, H, W = imgs.shape
        results = {}

        imgs = imgs.reshape(B * V, 3, H, W)
        feats = self.feature(imgs, B, V)  # (B*V, 8, H, W), (B*V, 16, H//2, W//2), (B*V, 32, H//4, W//4)

        for l in reversed(range(self.levels)):  # (2, 1, 0)
            feats_l = feats[f"level_{l}"]  # (B*V, C, h, w)
            feats_l = feats_l.view(B, V, *feats_l.shape[1:])  # (B, V, C, h, w)
            proj_mats_l = proj_mats[:, :, l]  # (B, V-1, 3, 4)
            depth_interval_l = depth_interval * self.interval_ratios[l]
            D = self.n_depths[l]
            if l == self.levels - 1:  # coarsest level
                h, w = feats_l.shape[-2:]
                if isinstance(init_depth_min, float):
                    depth_values = init_depth_min + depth_interval_l * torch.arange(0, D, device=imgs.device,
                                                                                    dtype=imgs.dtype)  # (D)
                    depth_values = rearrange(depth_values, 'd -> 1 d 1 1')
                    depth_values = repeat(depth_values, '1 d 1 1 -> b d h w', b=B, h=h, w=w)
                else:
                    depth_values = init_depth_min + depth_interval_l * rearrange(
                        torch.arange(0, D, device=imgs.device, dtype=imgs.dtype), 'd -> 1 d')  # (B, D)
                    depth_values = rearrange(depth_values, 'b d -> b d 1 1')
                    depth_values = repeat(depth_values, 'b d 1 1 -> b d h w', h=h, w=w)
            else:
                depth_lm1 = depth_l.detach()  # the depth of previous level
                depth_lm1 = F.interpolate(rearrange(depth_lm1, 'b h w -> b 1 h w'), scale_factor=2, mode='bilinear',
                                          align_corners=True)  # (B, 1, h, w)
                depth_values = get_depth_values(depth_lm1, D, depth_interval_l)
                del depth_lm1
            depth_l, confidence_l = self.predict_depth(feats_l, proj_mats_l, depth_values,
                                                       getattr(self, f'cost_reg_{l}'))
            del feats_l, proj_mats_l, depth_values
            results[f"depth_{l}"] = depth_l
            results[f"confidence_{l}"] = confidence_l

        return results
