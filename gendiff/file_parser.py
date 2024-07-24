import yaml
import json


def parse_file(path_to_file: str):
    """
    Returns the file data as a dictionary.

    For files with the extensions .json and .yaml.
    For other extensions, it returns a dictionary containing only
    'Exception': 'file has wrong format'.
    """
    if path_to_file.endswith('.yml') or path_to_file.endswith('.yaml'):
        with open(path_to_file) as file_to_parse:
            result = yaml.load(file_to_parse, Loader=yaml.FullLoader)
    elif path_to_file.endswith('.json'):
        with open(path_to_file) as file_to_parse:
            result = json.load(file_to_parse)
    else:
        result = {'Exception': 'file has wrong format'}
    return result
