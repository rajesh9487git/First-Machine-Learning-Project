from housing.exception import HousingException
import os,sys
from housing.logger import logging
from housing.entity.config_entity import DataValidationConfig, DataIngestionConfig
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
import pandas as pd


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

            data_ingestion_config= DataIngestionConfig
            original_dataset_df=pd.read_csv(data_ingestion_config.raw_data_dir)
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            # validating the column count

            df_columns_count=original_dataset_df.shape[1]
            train_columns_count=train_df.shape[1]
            test_columns_count=test_df.shape[1]

            is_train_column_count_correct=False
            is_test_column_count_correct=False
            is_column_count_correct= False




            if df_columns_count==train_columns_count:
                is_train_column_count_correct=True
            


            if df_columns_count==test_columns_count:
                is_test_column_count_correct=True
              


            is_column_count_correct= is_train_column_count_correct and is_test_column_count_correct


            # checking the value of ocean proximity
            
            original_ocean_proximity= original_dataset_df.ocean_proximity.unique()
            set_of_original_ocean_proximity= set(original_ocean_proximity) 

            train_ocean_proximity= train_df.ocean_proximity.unique()
            set_of_train_ocean_proximity= set(train_ocean_proximity) 

            test_ocean_proximity= test_df.ocean_proximity.unique()
            set_of_test_ocean_proximity= set(test_ocean_proximity) 

            is_column_value_correct= False
            is_train_column_value_correct= False
            is_test_column_value_correct= False


            if set_of_original_ocean_proximity==set_of_train_ocean_proximity:
                is_train_column_value_correct= True

            if set_of_original_ocean_proximity==set_of_test_ocean_proximity:
                is_test_column_value_correct= True    


            is_column_value_correct = is_train_column_value_correct and  is_test_column_value_correct

            # validating the column names

            original_column_names= original_dataset_df.columns
            train_column_names = train_df.columns
            test_column_names= test_df.columns

            is_column_names_correct= False
            is_train_column_names_correct= False
            is_test_column_names_correct= False

            if original_column_names == train_column_names:
                is_train_column_names_correct= True

            if original_column_names == test_column_names:
                is_test_column_names_correct= True   


            is_column_names_correct = is_train_column_names_correct and is_test_column_names_correct

            validation_status = is_column_count_correct and is_column_value_correct and is_column_names_correct

            #validation_status = True
            return validation_status 
        except Exception as e:
            raise HousingException(e,sys) from e


    def initiate_data_validation(self)-> DataValidationArtifact:

        try: 

            self.is_train_test_file_exists()
            self.validate_dataset_schema()

        except Exception as e:
            raise HousingException(e, sys) from e












                 