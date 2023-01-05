FROM docker.io/nvidia/cuda:11.7.0-runtime-ubuntu18.04

ENV DEBIAN_FRONTEND="noninteractive"
ENV PYTHONUNBUFFERED="1"

ENV WEBUI_REPO_URL="https://github.com/AUTOMATIC1111/stable-diffusion-webui.git"
ENV PYTHON_VERSION="3.10"

ENV WORKDIR="/workspace"
ENV VIRTUAL_ENV="${WORKDIR}/venv"

RUN apt update && apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt install -y \
  git \
  libgl1 \
  python3-pip \
  python${PYTHON_VERSION} \
  python${PYTHON_VERSION}-venv

RUN git clone --depth=1 ${WEBUI_REPO_URL} ${WORKDIR}
WORKDIR ${WORKDIR}

# install virtual env
RUN python${PYTHON_VERSION} -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

# install dependencies
# TODO: install xformers
RUN pip install --prefer-binary runpod
RUN python launch.py --exit --skip-torch-cuda-test

# cache huggingface transformers
COPY models/ models/
COPY cache.py .
RUN python cache.py &&\
  rm -rf models/* cache.py &&\
  git reset --hard
