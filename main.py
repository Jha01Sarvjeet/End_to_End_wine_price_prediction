from src.wine_qulity_predction import logger
from src.wine_qulity_predction.pipeline.Data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.wine_qulity_predction.pipeline.Data_validation_pipeline import DataValidatioinTrainingPipeline
from src.wine_qulity_predction.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
STAGE_NAME='Data Ingestion stage'
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} started<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_igestion()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Completed<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e
    

STAGE_NAME='Data Validation stage'
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} started<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    data_validation=DataValidatioinTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Completed<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e
    
    
STAGE_NAME='Data Transformation stage'
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} started<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Completed<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e
    