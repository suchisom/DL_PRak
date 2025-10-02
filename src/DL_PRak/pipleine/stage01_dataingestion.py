from DL_PRak.config import ConfigurationManager
from DL_PRak.components import DataIngestion
from DL_PRak import logger

class DataingestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.unzip_and_clean()
            