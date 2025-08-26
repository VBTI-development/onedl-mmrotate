# Copyright (c) OpenMMLab. All rights reserved.

import numpy as np
import torch
from loguru import logger
from mmdet.datasets.onedl import OneDLDataset
from onedl.core import (InstanceSegmentationInstances, LabelMap,
                        ObjectDetectionInstances)
from typing import Literal, Union

from mmrotate.registry import DATASETS
from mmrotate.structures.bbox import rbox2qbox


@DATASETS.register_module()
class OneDLOBBDataset(OneDLDataset):
    """Wrapper for OneDL Oriented Bounding Box datasets to mmrotate.

    For more information about OneDL datasets, please refer to
    https://onedl.ai.
    """

    def __init__(self,
                 *args,
                 rbb_format: Literal['qbox', 'rbox'] = 'rbox',
                 **kwargs):
        """Load rotated bounding box dataset.

        For args see mmdet.OneDLDataset.
            rbb_format: which format to output the bounding box in.
                rbox: rotated box with shape (..., 5)
                qbox: quadrilateral box with shape (..., 8)
        """
        self.rbb_format = rbb_format
        super().__init__(*args, **kwargs)

    def _preprocess_dataset(self, dataset):
        if self.min_bbox_area > 0:
            logger.info(
                f"Filtering dataset '{self.dataset_name}' bboxes by surface "
                f'({self.min_bbox_area}<).')
            dataset.filter_by_sqrt_area(self.min_bbox_area, inplace=True)

    def _to_mm_instance(self, instances: Union[ObjectDetectionInstances,
                                               InstanceSegmentationInstances],
                        label_map: LabelMap):
        mm_instances = []
        for annotation in instances:
            mm_instance = dict()

            bbox = annotation.bbox.as_cxcywh_theta90(return_type='list')
            # convert from degrees to rads
            bbox[-1] = np.deg2rad(bbox[-1])
            if self.rbb_format == 'qbox':
                bbox = rbox2qbox(torch.from_numpy(
                    np.array(bbox))).numpy().tolist()[0]

            mm_instance['bbox'] = bbox
            class_id = label_map.label_to_class_id(annotation.label)
            mm_instance['bbox_label'] = class_id
            mm_instance['ignore_flag'] = False
            mm_instances.append(mm_instance)
        return mm_instances
