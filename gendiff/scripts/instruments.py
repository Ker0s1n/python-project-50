#!/usr/bin/env python3
import yaml
import json


def is_dict(value):
    return type(value) is dict


def exception_format_difference(value):
    match value:
        case None: return 'null'
        case False: return 'false'
        case True: return 'true'
        case _: return value


def exception_format_plain(value):
    if value in ['true', 'false', 'null', '[complex value]']:
        return value
    elif type(value) is int:
        return value
    else:
        return f"'{str(value)}'"


def exception_format_json(value):
    if value in ['true', 'false', 'null']:
        return value
    else:
        return f'"{str(value)}"'


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


def make_value_for_key(
        key, value, another_value, node, another_node, function, depth):
    if key not in node:
        return {'type': 'added', 'value': another_value}
    elif key not in another_node:
        return {'type': 'deleted', 'value': value}
    elif is_dict(value) and is_dict(another_value):
        return {
            'type': 'nested',
            'value': function(value, another_value, depth + 1)}
    else:
        if value != another_value:
            return {
                'type': 'changed',
                'old_value': value,
                'new_value': another_value}
        else:
            return {'type': 'unchanged', 'value': value}


def make_diff(file1, file2):
    input1 = parse_file(file1)
    input2 = parse_file(file2)

    def walk(node1, node2, depth: int = 0):
        result = {}
        for key in sorted(node1.keys() | node2.keys()):
            value1 = exception_format_difference(node1.get(key))
            value2 = exception_format_difference(node2.get(key))
            result[key] = make_value_for_key(
                key, value1, value2, node1, node2, walk, depth)
        return result
    return walk(input1, input2, 0)
