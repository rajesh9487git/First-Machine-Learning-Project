import yaml
import os, sys
from housing.exception import HousingException


def read_yaml_file(file_path:str)-> dict:

    # Reads a YAML file and returns the content of the dict

    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise HousingException(e, sys) from e
        



