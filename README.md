<div align="center">  <picture>
    <!-- User prefers dark mode: -->
  <source srcset="https://raw.githubusercontent.com/vbti-development/onedl-mmrotate/main/docs/en/_static/image/onedl-mmrotate-banner-dark.png"  media="(prefers-color-scheme: dark)"/>

<img src="https://raw.githubusercontent.com/vbti-development/onedl-mmrotate/main/docs/en/_static/image/onedl-mmrotate-banner.png" alt="OneDL-Rotate logo" height="200"/>
  </picture>

<div>&nbsp;</div>
  <div align="center">
    <a href="https://vbti.ai">
      <b><font size="5">VBTI Website</font></b>
    </a>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://onedl.ai">
      <b><font size="5">OneDL platform</font></b>
    </a>
  </div>
<div>&nbsp;</div>

[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://onedl-mmrotate.readthedocs.io/en/latest/)
[![license](https://img.shields.io/github/license/VBTI-development/onedl-mmrotate.svg)](https://github.com/VBTI-development/onedl-mmrotate/blob/main/LICENSE)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/onedl-mmrotate)](https://pypi.org/project/onedl-mmrotate/)
[![PyPI](https://img.shields.io/pypi/v/onedl-mmrotate)](https://pypi.org/project/onedl-mmrotate)

[![Build Status](https://github.com/VBTI-development/onedl-mmrotate/actions/workflows/merge_stage_test.yml/badge.svg)](https://github.com/VBTI-development/onedl-mmrotate/actions/workflows/merge_stage_test.yml)
[![open issues](https://isitmaintained.com/badge/open/VBTI-development/onedl-mmrotate.svg)](https://github.com/VBTI-development/onedl-mmrotate/issues)
[![issue resolution](https://isitmaintained.com/badge/resolution/VBTI-development/onedl-mmrotate.svg)](https://github.com/VBTI-development/onedl-mmrotate/issues)

[📘Documentation](https://onedl-mmrotate.readthedocs.io/en/latest/) |
[🛠️Installation](https://onedl-mmrotate.readthedocs.io/en/latest/install.html) |
[👀Model Zoo](https://onedl-mmrotate.readthedocs.io/en/latest/model_zoo.html) |
[🆕Update News](https://onedl-mmrotate.readthedocs.io/en/latest/notes/changelog.html) |
[🚀Ongoing Projects](https://github.com/vbti-development/onedl-mmrotate/projects) |
[🤔Reporting Issues](https://github.com/vbti-development/onedl-mmrotate/issues/new/choose)

[![Discord Logo](https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/66e3d80db9971f10a9757c99_Symbol.svg)](https://discord.gg/8DvcVRs5Pm)

</div>

## Introduction

MMRotate is an open-source toolbox for rotated object detection based on PyTorch.

The master branch works with **PyTorch 2.0+**.

https://user-images.githubusercontent.com/10410257/154433305-416d129b-60c8-44c7-9ebb-5ba106d3e9d5.MP4

<details open>
<summary><b>Major Features</b></summary>

- **Support multiple angle representations**

  MMRotate provides three mainstream angle representations to meet different paper settings.

- **Modular Design**

  We decompose the rotated object detection framework into different components,
  which makes it much easy and flexible to build a new model by combining different modules.

- **Strong baseline and State of the art**

  The toolbox provides strong baselines and state-of-the-art methods in rotated object detection.

</details>

## What's New

### Highlight

The VBTI development team is reviving MMLabs code, making it work with
newer pytorch versions and fixing bugs. We are only a small team, so your help
is appreciated.

We are excited to announce our latest work on real-time object recognition tasks, **RTMDet**, a family of fully convolutional single-stage detectors. RTMDet not only achieves the best parameter-accuracy trade-off on object detection from tiny to extra-large model sizes but also obtains new state-of-the-art performance on instance segmentation and rotated object detection tasks. Details can be found in the [technical report](https://arxiv.org/abs/2212.07784). Pre-trained models are [here](configs/rotated_rtmdet).

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/rtmdet-an-empirical-study-of-designing-real/real-time-instance-segmentation-on-mscoco)](https://paperswithcode.com/sota/real-time-instance-segmentation-on-mscoco?p=rtmdet-an-empirical-study-of-designing-real)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/rtmdet-an-empirical-study-of-designing-real/object-detection-in-aerial-images-on-dota-1)](https://paperswithcode.com/sota/object-detection-in-aerial-images-on-dota-1?p=rtmdet-an-empirical-study-of-designing-real)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/rtmdet-an-empirical-study-of-designing-real/object-detection-in-aerial-images-on-hrsc2016)](https://paperswithcode.com/sota/object-detection-in-aerial-images-on-hrsc2016?p=rtmdet-an-empirical-study-of-designing-real)

| Task                     | Dataset | AP                                   | FPS(TRT FP16 BS1 3090) |
| ------------------------ | ------- | ------------------------------------ | ---------------------- |
| Object Detection         | COCO    | 52.8                                 | 322                    |
| Instance Segmentation    | COCO    | 44.6                                 | 188                    |
| Rotated Object Detection | DOTA    | 78.9(single-scale)/81.3(multi-scale) | 121                    |

<div align=center>
<img src="https://user-images.githubusercontent.com/12907710/208044554-1e8de6b5-48d8-44e4-a7b5-75076c7ebb71.png"/>
</div>

**v1.0.0rc1** was released in 30/12/2022:

- Support [RTMDet](configs/rotated_rtmdet) rotated object detection models. The technical report of RTMDet is on [arxiv](https://arxiv.org/abs/2212.07784)
- Support [H2RBox](configs/h2rbox) models. The technical report of H2RBox is on [arxiv](https://arxiv.org/abs/2210.06742)

## Installation

Please refer to [Installation](https://onedl-mmrotate.readthedocs.io/en/latest/get_started.html) for more detailed instruction.

## Getting Started

Please see [Overview](https://onedl-mmrotate.readthedocs.io/en/latest/overview.html) for the general introduction of MMRotate.

For detailed user guides and advanced guides, please refer to our [documentation](https://onedl-mmrotate.readthedocs.io/en/latest/):

- User Guides
  - [Train & Test](https://onedl-mmrotate.readthedocs.io/en/latest/user_guides/index.html#train-test)
    - [Learn about Configs](https://onedl-mmrotate.readthedocs.io/en/latest/user_guides/config.html)
    - [Inference with existing models](https://onedl-mmrotate.readthedocs.io/en/latest/user_guides/inference.html)
    - [Dataset Prepare](https://onedl-mmrotate.readthedocs.io/en/latest/user_guides/dataset_prepare.html)
    - [Test existing models on standard datasets](https://onedl-mmrotate.readthedocs.io/en/latest/user_guides/train_test.html)
    - [Train predefined models on standard datasets](https://onedl-mmrotate.readthedocs.io/en/latest/user_guides/train_test.html)
    - [Test Results Submission](https://onedl-mmrotate.readthedocs.io/en/latest/user_guides/test_results_submission.html)
  - [Useful Tools](https://onedl-mmrotate.readthedocs.io/en/latest/user_guides/index.html#useful-tools)
- Advanced Guides
  - [Basic Concepts](https://onedl-mmrotate.readthedocs.io/en/latest/advanced_guides/index.html#basic-concepts)
  - [Component Customization](https://onedl-mmrotate.readthedocs.io/en/latest/advanced_guides/index.html#component-customization)
  - [How to](https://onedl-mmrotate.readthedocs.io/en/latest/advanced_guides/index.html#how-to)

We also provide colab tutorial [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](demo/MMRotate_Tutorial.ipynb).

To migrate from MMRotate 0.x, please refer to [migration](https://onedl-mmrotate.readthedocs.io/en/latest/migration.html).

## Model Zoo

Results and models are available in the *README.md* of each method's config directory.
A summary can be found in the [Model Zoo](docs/en/model_zoo.md) page.

<details open>
<summary><b>Supported algorithms:</b></summary>

- [x] [Rotated RetinaNet-OBB/HBB](configs/rotated_retinanet/README.md) (ICCV'2017)
- [x] [Rotated FasterRCNN-OBB](configs/rotated_faster_rcnn/README.md) (TPAMI'2017)
- [x] [Rotated RepPoints-OBB](configs/rotated_reppoints/README.md) (ICCV'2019)
- [x] [Rotated FCOS](configs/rotated_fcos/README.md) (ICCV'2019)
- [x] [RoI Transformer](configs/roi_trans/README.md) (CVPR'2019)
- [x] [Gliding Vertex](configs/gliding_vertex/README.md) (TPAMI'2020)
- [x] [Rotated ATSS-OBB](configs/rotated_atss/README.md) (CVPR'2020)
- [x] [CSL](configs/csl/README.md) (ECCV'2020)
- [x] [R<sup>3</sup>Det](configs/r3det/README.md) (AAAI'2021)
- [x] [S<sup>2</sup>A-Net](configs/s2anet/README.md) (TGRS'2021)
- [x] [ReDet](configs/redet/README.md) (CVPR'2021)
- [x] [Beyond Bounding-Box](configs/cfa/README.md) (CVPR'2021)
- [x] [Oriented R-CNN](configs/oriented_rcnn/README.md) (ICCV'2021)
- [x] [GWD](configs/gwd/README.md) (ICML'2021)
- [x] [KLD](configs/kld/README.md) (NeurIPS'2021)
- [x] [SASM](configs/sasm_reppoints/README.md) (AAAI'2022)
- [x] [Oriented RepPoints](configs/oriented_reppoints/README.md) (CVPR'2022)
- [x] [KFIoU](configs/kfiou/README.md) (ICLR'2023)
- [x] [H2RBox](configs/h2rbox/README.md) (ICLR'2023)
- [x] [PSC](configs/psc/README.md) (CVPR'2023)
- [x] [RTMDet](configs/rotated_rtmdet/README.md) (arXiv)
- [x] [H2RBox-v2](configs/h2rbox_v2/README.md) (arXiv)

</details>

## Data Preparation

Please refer to [data_preparation.md](tools/data/README.md) to prepare the data.

## FAQ

Please refer to [FAQ](docs/en/notes/faq.md) for frequently asked questions.

## Contributing

We appreciate all contributions to improve MMRotate. Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing guideline.

## Acknowledgement

MMRotate is an open source project that is contributed by researchers and engineers from various colleges and companies. We appreciate all the contributors who implement their methods or add new features, as well as users who give valuable feedbacks. We appreciate the [Student Innovation Center of SJTU](https://www.si.sjtu.edu.cn/) for providing rich computing resources at the beginning of the project. We wish that the toolbox and benchmark could serve the growing research community by providing a flexible toolkit to reimplement existing methods and develop their own new methods.

## Citation

If you use this toolbox or benchmark in your research, please cite this project.

```bibtex
@inproceedings{zhou2022mmrotate,
  title   = {MMRotate: A Rotated Object Detection Benchmark using PyTorch},
  author  = {Zhou, Yue and Yang, Xue and Zhang, Gefan and Wang, Jiabao and Liu, Yanyi and
             Hou, Liping and Jiang, Xue and Liu, Xingzhao and Yan, Junchi and Lyu, Chengqi and
             Zhang, Wenwei and Chen, Kai},
  booktitle={Proceedings of the 30th ACM International Conference on Multimedia},
  pages = {7331–7334},
  numpages = {4},
  year={2022}
}
```

## License

This project is released under the [Apache 2.0 license](LICENSE).

## Projects in VBTI-development

- [MMEngine](https://github.com/vbti-development/onedl-mmengine): Foundational library for training deep learning models.
- [MMCV](https://github.com/vbti-development/onedl-mmcv): Foundational library for computer vision.
- [MMPreTrain](https://github.com/vbti-development/onedl-mmpretrain): Pre-training toolbox and benchmark.
- [MMDetection](https://github.com/vbti-development/onedl-mmdetection): Detection toolbox and benchmark.
- [MMRotate](https://github.com/vbti-development/onedl-mmrotate): Rotated object detection toolbox and benchmark.
- [MMSegmentation](https://github.com/vbti-development/onedl-mmsegmentation): Semantic segmentation toolbox and benchmark.
- [MMDeploy](https://github.com/vbti-development/onedl-mmdeploy): Model deployment framework.
- [MIM](https://github.com/vbti-development/onedl-mim): MIM installs VBTI packages.
