#!/usr/bin/env python3
import yaml
import json


def is_dict(value):
    return type(value) is dict


def revert_exceptions(value):
    match value:
        case None: return 'null'
        case False: return 'false'
        case True: return 'true'
        case _: return value


def parse_file(path_to_file: str):
    if '.yml' in path_to_file or '.yaml' in path_to_file:
        with open(path_to_file) as file_to_parse:
            result = yaml.load(file_to_parse, Loader=yaml.FullLoader)
    elif '.json' in path_to_file:
        with open(path_to_file) as file_to_parse:
            result = json.load(file_to_parse)
    else:
        result = {'Exception': 'file has wrong format'}
    return result


def make_diff(file1, file2):
    input1 = parse_file(file1)
    input2 = parse_file(file2)

    def walk(node1, node2, depth: int = 0):
        result = {}
        for key in sorted(node1.keys() | node2.keys()):
            value1 = revert_exceptions(node1.get(key))
            value2 = revert_exceptions(node2.get(key))

            if key not in node1:
                result[key] = {'type': 'added',
                               'value': value2}
            elif key not in node2:
                result[key] = {'type': 'deleted',
                               'value': value1}
            elif is_dict(value1) and is_dict(value2):
                result[key] = {'type': 'nested',
                               'value': walk(value1, value2, depth + 1)}
            else:
                if value1 != value2:
                    result[key] = {'type': 'changed',
                                   'old_value': value1, 'new_value': value2}
                else:
                    result[key] = {'type': 'unchanged',
                                   'value': value1}
        return result
    return walk(input1, input2, 0)
