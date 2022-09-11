from housing.exception import HousingException
import os,sys
from housing.logger import logging
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact


class DataVaidation():
    def __init__(self, data_validation_config:DataValidationConfig,data_ingestion_artifact: DataIngestionArtifact):
        try:

            logging.info(f"{'>>'*30}Data Valdaition log started.{'<<'*30} \n\n")
            self.data_validation_config= data_validation_config
            self.data_ingestion_artifact= data_ingestion_artifact

        except Exception() as e:
            raise HousingException(e, sys)    



    def get_train_and_test_df(self):
        try:
            pass

        except Exception as e:
            raise HousingException(e, sys)   


    def is_train_test_file_exists(self)-> bool:
        try:

            logging.info("checking if training and test file is available") 
            is_train_file_exist= False
            is_test_file_exist= False

            train_file_path= self.data_ingestion_artifact.train_file_path
            test_file_path=  self.data_ingestion_artifact.test_file_path

            is_train_file_exist= os.path.exists(train_file_path)    
            is_test_file_exist= os.path.exists(test_file_path)     

            is_available=  is_train_file_exist and is_test_file_exist

            logging.info(f"is train and test file exists?->{is_available}")

            if not is_available:
                training_file= train_file_path
                testing_file= test_file_path

                message= f"Training file : {training_file} or Testing file :{testing_file} is not present"


                raise Exception("message")

            return is_available

        except Exception as e:
            raise HousingException(e, sys) from e  



    def validate_dataset_schema(self)-> bool:
        try:
            validation_status = False
            
            #Assigment validate training and testing dataset using schema file
            #1. Number of Column
            #2. Check the value of ocean proximity 
            # acceptable values     <1H OCEAN
            # INLAND
            # ISLAND
            # NEAR BAY
            # NEAR OCEAN
            #3. Check column names


            validation_status = True
            return validation_status 
        except Exception as e:
            raise HousingException(e,sys) from e


    def initiate_data_validation(self)-> DataValidationArtifact:

        try: 

            self.is_train_test_file_exists()
            self.validate_dataset_schema()

        except Exception as e:
            raise HousingException(e, sys) from e












                 