from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_validation import DataValidation
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.config_entity import DataIngestionConfig,DataValidationConfig
from network_security.entity.config_entity import TrainingPipelineConfig


if __name__ == "__main__":
    try:
       training_pipeline_config = TrainingPipelineConfig()
       data_ingestion_config = DataIngestionConfig(training_pipeline_config)
       data_ingestion = DataIngestion(data_ingestion_config)
       logging.info("Initiate the data ingestion")
       data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
       logging.info("Data initiation completed")
       print(data_ingestion_artifact)
       data_validation_config = DataValidationConfig(training_pipeline_config)
       data_validation = DataValidation(data_ingestion_artifact,data_validation_config)
       logging.info("initiate data validation")
       data_validation_artifact = data_validation.inititate_data_valiation()
       logging.info("data validation completed")
       print(data_validation_artifact)
      

    except Exception as e:
        raise NetworkSecurityException(e,sys)