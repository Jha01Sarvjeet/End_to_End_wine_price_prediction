from src.wine_qulity_predction import logger
from src.wine_qulity_predction.pipeline.Data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME='Data Ingestion stage'
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} started<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_igestion()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Completed<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e
    