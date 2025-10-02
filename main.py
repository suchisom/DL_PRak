from DL_PRak.pipleine.stage01_dataingestion import DataingestionTrainingPipeline
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
    