import tensorflow as tf
from DL_PRak.pipeline.stage01_dataingestion import DataingestionTrainingPipeline
from DL_PRak.pipeline.stage02_preparemodel import PrepareBaseModelTrainingPipeline
from DL_PRak.pipeline.stage03_training import ModelTrainingPipeline
from DL_PRak.pipeline.stage04_evaluation import EvaluationPipeline

from DL_PRak import logger

STAGE_NAME = "data ingestion stage"
try: 
    logger.info(f'>>>>>>> stage {STAGE_NAME} start <<<<<<')
    data_ingestion = DataingestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>> {STAGE_NAME} completed <<<<<<')
except Exception as e :
    logger.exception(e)
    raise e 



STAGE_NAME = "Prepare base model"
try: 
    logger.info(f'******************************')
    logger.info(f'>>>>>>> stage {STAGE_NAME} start <<<<<<')
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f'>>>>>>>> {STAGE_NAME} completed <<<<<<')

except Exception as e :
    logger.exception(e)
    raise e 
    


STAGE_NAME = "Training"
try:
    logger.info(f'******************************')
    logger.info(f'>>>>>>> stage {STAGE_NAME} start <<<<<<')
    prepare_base_model = ModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f'>>>>>>>> {STAGE_NAME} completed <<<<<<')

except Exception as e :
    logger.exception(e)
    raise e 
    


STAGE_NAME = "evaluation"
try:
    logger.info(f'******************************')
    logger.info(f'>>>>>>> stage {STAGE_NAME} start <<<<<<')
    model_evalutaion = EvaluationPipeline()
    prepare_base_model.main()
    logger.info(f'>>>>>>>> {STAGE_NAME} completed <<<<<<')

except Exception as e :
    logger.exception(e)
    raise e 