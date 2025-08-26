# Copyright (c) OpenMMLab. All rights reserved.
from .dior import DIORDataset  # noqa: F401, F403
from .dota import DOTAv2Dataset  # noqa: F401, F403
from .dota import DOTADataset, DOTAv15Dataset
from .hrsc import HRSCDataset  # noqa: F401, F403

try:
    from .onedl import OneDLOBBDataset
    onedl_dataset_types = ['OneDLOBBDataset']
except ImportError:
    import logging
    from mmengine.logging import print_log
    print_log('Could not import OneDL', level=logging.DEBUG)
    onedl_dataset_types = []

from .transforms import *  # noqa: F401, F403

__all__ = [
    'DOTADataset',
    'DOTAv15Dataset',
    'DOTAv2Dataset',
    'HRSCDataset',
    'DIORDataset',
] + onedl_dataset_types
