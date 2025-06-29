from src.wine_qulity_predction.config.configuration import ConfiguarationManager
from src.wine_qulity_predction.components.data_ingestion import DataIngestion
from src.wine_qulity_predction import logger

STAGE_NAME="Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_igestion(self):
         config=ConfiguarationManager()
         data_ingestion_config=config.get_data_ingestion_config()
         data_inegestion=DataIngestion(data_ingestion_config)
         data_inegestion.download_file()
         data_inegestion.zip_file_extract()
