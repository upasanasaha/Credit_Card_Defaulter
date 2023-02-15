from predictor.logger import logging
from predictor.exception import SensorException
from predictor.utils import get_collection_as_dataframe
import sys,os
from predictor.entity import config_entity
from predictor.components.data_ingestion import DataIngestion
# from predictor.components.data_validation import DataValidation
# from predictor.components.data_transformation import DataTransformation
# from predictor.components.model_trainer import ModelTrainer
# from predictor.components.model_evaluation import ModelEvaluation
# from predictor.components.model_pusher import ModelPusher

if __name__=="__main__":
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()
          
        #data ingestion
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
    except Exception as e:
        raise SensorException(e,sys)