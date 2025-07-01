from src.wine_qulity_predction import logger
from src.wine_qulity_predction.pipeline.Data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.wine_qulity_predction.pipeline.Data_validation_pipeline import DataValidatioinTrainingPipeline
from src.wine_qulity_predction.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.wine_qulity_predction.pipeline.model_training_pipeline import ModelTrainingPipeline
from src.wine_qulity_predction.pipeline.model_evaluation_pipeline import ModelEvaluation, ModelEvaluationPipeline

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

STAGE_NAME = 'model Training stage'
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} started<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    data_transformation = ModelTrainingPipeline()
    data_transformation.initiate_model_training()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Completed<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'model Evalutaion stage'
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} started<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    data_validation = ModelEvaluationPipeline()
    data_validation.start_model_evaluation_pipeline()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} Completed<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

