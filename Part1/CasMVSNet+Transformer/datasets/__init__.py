from .dtu import DTUDataset
from .tanks import TanksDataset
from .blendedmvs import BlendedMVSDataset
from .dtu_eval import DTUEvalDataset
from .custom import CustomDataset

dataset_dict = {
    'dtu': DTUDataset,
    'tanks': TanksDataset,
    'blendedmvs': BlendedMVSDataset,
    'dtu_eval': DTUEvalDataset,
    'custom': CustomDataset
}
