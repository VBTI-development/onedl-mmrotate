ARG PYTORCH="2.8.0"
ARG CUDA="12.0"
ARG CUDNN=""

FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-devel

ENV TORCH_CUDA_ARCH_LIST="6.0 6.1 7.0+PTX"
ENV TORCH_NVCC_FLAGS="-Xfatbin -compress-all"
ENV CMAKE_PREFIX_PATH="$(dirname $(which conda))/../"

# To fix GPG key error when running apt-get update
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub

RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install onedl-mim
RUN pip install --no-cache-dir -U onedl-mim
# Install onedl-mmengine, onedl-mmcv, and onedl-mmdetection
RUN mim install --no-cache-dir onedl-mmengine "onedl-mmcv>=2.0.0rc2" "onedl-mmdetection>=3.0.0rc2"
# Install MMRotate
RUN conda clean --all -y
RUN git clone https://github.com/vbti-development/onedl-mmrotate.git /mmrotate
WORKDIR /mmrotate
ENV FORCE_CUDA="1"
RUN pip install -r pyproject.toml --group build
RUN pip install --no-cache-dir -e .
