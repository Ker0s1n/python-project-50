#!/usr/bin/env python3
import yaml
import json


def parse_file(path_to_file: str):
    if path_to_file.endswith('.yml') or path_to_file.endswith('.yaml'):
        with open(path_to_file) as file_to_parse:
            result = yaml.load(file_to_parse, Loader=yaml.FullLoader)
    elif path_to_file.endswith('.json'):
        with open(path_to_file) as file_to_parse:
            result = json.load(file_to_parse)
    else:
        result = {'Exception': 'file has wrong format'}
    return result
