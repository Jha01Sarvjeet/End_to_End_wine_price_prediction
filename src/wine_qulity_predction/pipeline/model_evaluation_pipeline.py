from src.wine_qulity_predction.config.configuration import ConfiguarationManager
from src.wine_qulity_predction.components.model_evaluation import ModelEvaluation
from src.wine_qulity_predction import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def start_model_evaluation_pipeline(self):
        config = ConfiguarationManager()
        model_evaluation_config = config.get_model_evaluation_config()

        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()