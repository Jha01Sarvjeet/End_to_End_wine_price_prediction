from src.wine_qulity_predction.config.configuration import ConfiguarationManager
from src.wine_qulity_predction.components.data_validation import DataValidation
from src.wine_qulity_predction import logger

STAGE_NAME="Data Ingestion stage"


class DataValidatioinTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_validation(self):
         config=ConfiguarationManager()
         data_validation_config=config.get_data_validation_config()
         data_validation=DataValidation(data_validation_config)
         data_validation.valiadate_all_columns()
      
