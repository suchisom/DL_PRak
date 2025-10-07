from DL_PRak.config import ConfigurationManager
from DL_PRak.components import PrepareBaseModel
from DL_PRak import logger

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
            config = ConfigurationManager()
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()

    
   

            
        
            
            