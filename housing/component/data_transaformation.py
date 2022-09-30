from cgi import test
from sklearn import preprocessing
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import DataTransformationConfig 
from housing.entity.artifact_entity import DataIngestionArtifact,\
DataValidationArtifact,DataTransformationArtifact
import sys,os
import numpy as np
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import pandas as pd
from housing.constant import *
from housing.util.util import read_yaml_file,save_object,save_numpy_array_data,load_data

#   longitude: float
#   latitude: float
#   housing_median_age: float
#   total_rooms: float
#   total_bedrooms: float
#   population: float
#   households: float
#   median_income: float
#   median_house_value: float
#   ocean_proximity: category
#   income_cat: float

class FeatureGenerator(BaseEstimator, TransformerMixin()):

    def __init__(self, add_bedroom_per_room=True,
                 total_rooms_ix=3,
                 population_ix=5,
                 households_ix=6,
                 total_bedrooms_ix=4, columns=None):


     """
        FeatureGenerator Initialization
        add_bedrooms_per_room: bool
        total_rooms_ix: int index number of total rooms columns
        population_ix: int index number of total population columns
        households_ix: int index number of  households columns
        total_bedrooms_ix: int index number of bedrooms columns
        """


        try:
            self.columns=columns
            if self.columns is not None:
                total_rooms_ix= self.columns.index(COLUMN_TOTAL_ROOMS)
                population_ix= self.columns.index(COLUMN_POPULATION)
                households_ix= self.columns.index(COLUMN_HOUSEHOLDS)
                total_bedrooms_ix= self.columns.index(COLUMN_HOUSEHOLDS)

            
            self.add_bedroom_per_room=add_bedroom_per_room
            self.total_rooms_ix=total_rooms_ix
            self.population_ix= population_ix
            self.households_ix= households_ix
            self.total_bedrooms_ix= total_bedrooms_ix

        except Exception as e:
            raise HousingException(e, sys) from e


    def fit(self, x, y=None):
        return self


    def transform(self, x, y=None) :
        try:

            room_per_household = x[:,self.total_rooms_ix]/ x[:, self.households_ix]
            population_per_household=x[:, self.population_ix]/x[:, self.households_ix]

            if self.add_bedroom_per_room:
                bedrooms_per_room= x[:, self.total_bedrooms_ix]/ x[:, self.total_rooms_ix]

                generated_feature= np.c_[x,room_per_household, population_per_household, bedrooms_per_room]


            else:

                 generated_feature= np.c_[x,room_per_household, population_per_household]  

            return generated_feature

        except Exception as e:
            raise HousingException(e, sys)          




