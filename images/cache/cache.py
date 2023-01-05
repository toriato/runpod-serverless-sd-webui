from modules import paths, modelloader, sd_models

# setup models
modelloader.cleanup_models()
sd_models.setup_model()
sd_models.load_model()
