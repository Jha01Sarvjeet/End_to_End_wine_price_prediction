from src.wine_qulity_predction.config.configuration import ConfiguarationManager
from src.wine_qulity_predction.components.data_transformation import DataTransformation
from src.wine_qulity_predction import logger

STAGE_NAME="Data Ingestion stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):
         config=ConfiguarationManager()
         data_transformation_config=config.get_transformation_config()
         data_transformation=DataTransformation(data_transformation_config)
         data_transformation.train_test_splitting()
      
