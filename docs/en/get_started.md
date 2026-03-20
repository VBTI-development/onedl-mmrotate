# GET STARTED

## Prerequisites

In this section we demonstrate how to prepare an environment with PyTorch.

MMRotate works on Linux and Windows. It requires Python 3.10+, CUDA 11.8+ and PyTorch 2.0+.

```{note}
If you are experienced with PyTorch and have already installed it, just skip this part and jump to the [next section](#installation). Otherwise, you can follow these steps for the preparation.
```

**Step 0.** Download and install Miniconda from the [official website](https://docs.conda.io/en/latest/miniconda.html).

**Step 1.** Create a conda environment and activate it.

```shell
conda create --name onedllab python=3.10 -y
conda activate onedllab
```

**Step 2.** Install PyTorch following [official instructions](https://pytorch.org/get-started/locally/), e.g.

```shell
conda install pytorch==2.8.0 torchvision==0.23.0 cudatoolkit=12.9 -c pytorch
```

## Installation

We recommend that users follow our best practices to install MMRotate. However, the whole process is highly customizable. See [Customize Installation](#customize-installation) section for more information.

### Best Practices

**Step 0.** Install [OneDL MMEngine](https://github.com/vbti-development/onedl-mmengine) and [OneDL MMCV](https://github.com/vbti-development/onedl-mmcv) using [OneDL MIM](https://github.com/vbti-development/onedl-mim).

```shell
pip install -U onedl-mim
mim install onedl-mmengine
mim install "onedl-mmcv"
```

**Step 1.** Install [MMDetection](https://github.com/vbti-development/onedl-mmdetection) as a dependency.

```shell
mim install 'onedl-mmdetection'
```

Optionally, you could also build MMDetection from source in case you want to modify the code:

```shell
git clone https://github.com/vbti-development/onedl-mmdetection.git
cd onedl-mmdetection
pip install -v -e .
# "-v" means verbose, or more output
# "-e" means installing a project in editable mode,
# thus any local modifications made to the code will take effect without reinstallation.
```

**Step 2.** Install MMRotate.

Case a: If you develop and run mmrotate directly, install it from source:

```shell
git clone https://github.com/vbti-development/onedl-mmrotate.git
cd onedl-mmrotate
pip install -v -e .
# "-v" means verbose, or more output
# "-e" means installing a project in editable mode,
# thus any local modifications made to the code will take effect without reinstallation.
```

Case b: If you use mmrotate as a dependency or third-party package, install it with pip:

```shell
pip install onedl-mmrotate
```

### Verify the installation

To verify whether MMRotate is installed correctly, we provide some sample codes to run an inference demo.

**Step 1.** We need to download config and checkpoint files.

```shell
mim download onedl-mmrotate --config oriented-rcnn-le90_r50_fpn_1x_dota --dest .
```

The downloading will take several seconds or more, depending on your network environment. When it is done, you will find two files `oriented-rcnn-le90_r50_fpn_1x_dota.py` and `oriented_rcnn_r50_fpn_1x_dota_le90-6d2b2ce0.pth` in your current folder.

**Step 2.** Verify the inference demo.

Option (a). If you install mmrotate from source, just run the following command.

```shell
python demo/image_demo.py demo/demo.jpg oriented-rcnn-le90_r50_fpn_1x_dota.py oriented_rcnn_r50_fpn_1x_dota_le90-6d2b2ce0.pth --out-file result.jpg
```

You will see a new image `result.jpg` on your current folder, where rotated bounding boxes are plotted on cars, buses, etc.

Option (b). If you install mmrotate with pip, open you python interpreter and copy&paste the following codes.

```python
from mmdet.apis import init_detector, inference_detector
import mmrotate

config_file = 'oriented-rcnn-le90_r50_fpn_1x_dota.py'
checkpoint_file = 'oriented_rcnn_r50_fpn_1x_dota_le90-6d2b2ce0.pth'
model = init_detector(config_file, checkpoint_file, device='cuda:0')
inference_detector(model, 'demo/demo.jpg')
```

You will see a list of arrays printed, indicating the detected rotated bounding boxes.

### Customize Installation

#### CUDA versions

When installing PyTorch, you need to specify the version of CUDA. If you are not clear on which to choose, follow our recommendations:

- For Ampere-based NVIDIA GPUs, such as GeForce 30 series and NVIDIA A100, CUDA 11 is a must.
- For older NVIDIA GPUs, CUDA 11 is backward compatible, but CUDA 10.2 offers better compatibility and is more lightweight.

Please make sure the GPU driver satisfies the minimum version requirements. See [this table](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#cuda-major-component-versions__table-cuda-toolkit-driver-versions) for more information.

```{note}
Installing CUDA runtime libraries is enough if you follow our best practices, because no CUDA code will be compiled locally. However if you hope to compile MMCV from source or develop other CUDA operators, you need to install the complete CUDA toolkit from NVIDIA's [website](https://developer.nvidia.com/cuda-downloads), and its version should match the CUDA version of PyTorch. i.e., the specified version of cudatoolkit in `conda install` command.
```

#### Install MMCV without MIM

MMCV contains C++ and CUDA extensions, thus depending on PyTorch in a complex way. MIM solves such dependencies automatically and makes the installation easier. However, it is not a must.

To install MMCV with pip instead of MIM, please follow [MMCV installation guides](https://onedl-mmcv.readthedocs.io/en/latest/get_started/installation.html). This requires manually specifying a find-url based on PyTorch version and its CUDA version.

For example, the following command install mmcv built for PyTorch 2.8.x and CUDA 12.9.

```shell
pip install onedl-mmcv -f https://mmassets.onedl.ai/mmcv/dist/cu129/torch2.8/index.html
```

#### Install on Google Colab

[Google Colab](https://research.google.com/) usually has PyTorch installed,
thus we only need to install MMCV and MMDetection with the following commands.

**Step 1.** Install [OneDL MMCV](https://github.com/vbti-development/onedl-mmcv) and [OneDL MMDetection](https://github.com/vbti-development/onedl-mmdetection) using [OneDL MIM](https://github.com/vbti-development/onedl-mim).

```shell
!pip3 install -U onedl-mim
!mim install "onedl-mmcv"
!mim install 'onedl-mmdetection'
```

**Step 2.** Install MMRotate from the source.

```shell
!git clone https://github.com/vbti-development/onedl-mmrotate.git
%cd onedl-mmrotate
!pip install -e .
```

**Step 3.** Verification.

```python
import mmrotate
print(mmrotate.__version__)
# Example output: 1.x
```

```{note}
Within Jupyter, the exclamation mark `!` is used to call external executables and `%cd` is a [magic command](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-cd) to change the current working directory of Python.
```

#### Using MMRotate with Docker

We provide a [Dockerfile](https://github.com/vbti-development/onedl-mmrotate/tree/main/docker/Dockerfile) to build an image. Ensure that your [docker version](https://docs.docker.com/engine/install/) >=19.03.

```shell
# build an image with PyTorch 1.6, CUDA 10.1
# If you prefer other versions, just modified the Dockerfile
docker build -t onedl-mmrotate -f docker/Dockerfile .
```

Run it with

```shell
docker run --gpus all --shm-size=8g -it -v {DATA_DIR}:/onedl-mmrotate/data onedl-mmrotate
```

### Trouble shooting

If you have some issues during the installation, please first view the [FAQ](faq.md) page.
You may [open an issue](https://github.com/vbti-development/onedl-mmrotate/issues/new/choose) on GitHub if no solution is found.
