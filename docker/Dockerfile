ARG CU_VERSION="129"
ARG TORCH_VERSION="280"
ARG ONEDL_MMDET_VERSION="3.4.1"

FROM vbti/onedl-mmdetection-cu${CU_VERSION}-torch${TORCH_VERSION}:${ONEDL_MMDET_VERSION}

# Install OneDL-MMRotate
COPY . /onedl/onedl-mmrotate

WORKDIR /onedl/onedl-mmrotate
RUN mim install --no-cache-dir -e .[optional]

# Verify installation
RUN python -c "import mmrotate; print('mmrotate version:', mmrotate.__version__)"
