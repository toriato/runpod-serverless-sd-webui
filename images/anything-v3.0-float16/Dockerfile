FROM docker.io/aeon1337/runpod-serverless-sd-webui:cache

COPY models/ models/
COPY entrypoint.py ./

ENTRYPOINT [ "python", "entrypoint.py" ]
