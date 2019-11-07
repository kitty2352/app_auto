import yaml
import os

def ret_yaml_data(file_name):
    file_path = "../Data/" + file_name + '.yml'
    with open(file_path, 'r') as f:
        return yaml.load(f)