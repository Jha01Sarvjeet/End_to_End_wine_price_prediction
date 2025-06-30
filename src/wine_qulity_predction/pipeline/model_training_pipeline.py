from src.wine_qulity_predction.config.configuration import ConfiguarationManager
from src.wine_qulity_predction.components.model_trainer import ModelTrainer
from src.wine_qulity_predction import logger

STAGE_NAME = "Model training stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfiguarationManager()
        model_training_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_training_config)
        model_trainer.train()

