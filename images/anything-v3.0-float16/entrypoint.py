import json

from typing import Dict
from os import environ
from io import BytesIO

from runpod import serverless
from requests import post

from modules import paths, shared, modelloader, sd_models
from modules.processing import StableDiffusionProcessingTxt2Img, process_images

# setup models
modelloader.cleanup_models()
sd_models.setup_model()
sd_models.load_model()


def handler(event):
    kwargs: Dict[str, any] = event['input']
    p = process_images(
        StableDiffusionProcessingTxt2Img(
            sd_model=shared.sd_model,
            **kwargs
        )
    )

    assert len(p.images) > 0, 'image was not processed'
    assert len(p.images) < 2, 'batch processing is not supported'

    image_bytes = BytesIO()
    p.images[0].save(image_bytes, format='PNG')

    res = post(
        environ.get('DISCORD_WEBHOOK_URL'),
        files={
            'file': (
                'generated.png',
                image_bytes.getvalue()
            ),
            'payload_json': (
                None,
                json.dumps({
                    'username': 'RunPod serverless'
                })
            )
        }
    )

    assert res.ok, f'server returns {res.status_code}'

    return json.loads(res.text)


serverless.start({'handler': handler})
