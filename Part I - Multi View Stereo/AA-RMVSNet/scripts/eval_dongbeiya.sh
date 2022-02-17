#!/usr/bin/env bash
# Reference: https://github.com/QT-Zhu/AA-RMVSNet
inverse_depth=False

CUDA_VISIBLE_DEVICES=0 python eval.py \
        --dataset=custom \
        --batch_size=1 \
        --inverse_depth=${inverse_depth} \
        --numdepth=1024 \
        --interval_scale=0.2 \
        --max_h=600 \
        --max_w=800 \
        --image_scale=1.0 \
        --testpath=custom/ \
        --testlist=./lists/custom/dongbeiya_1024.txt \
        --loadckpt=./checkpoints/model_release.ckpt \
        --outdir=./outputs_dongbeiya_800_1024
