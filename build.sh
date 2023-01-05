#!/bin/bash
tag="${1}"
podman build -t "docker.io/aeon1337/runpod-serverless-sd-webui:${tag}" "./images/${tag}"
