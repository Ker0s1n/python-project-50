#!/usr/bin/env python3
import yaml
import json
from gendiff.scripts.argument_parser import parse_args
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


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


def make_value_for_difference(
        key, value, another_value, node, another_node, function, depth):
    if key not in node:
        return {'type': 'added', 'value': another_value}
    elif key not in another_node:
        return {'type': 'deleted', 'value': value}
    elif isinstance(value, dict) and isinstance(another_value, dict):
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


def difference(node1, node2, depth: int = 0):
    result = {}
    for key in sorted(node1.keys() | node2.keys()):
        value1 = node1.get(key)
        value2 = node2.get(key)
        result[key] = make_value_for_difference(
            key, value1, value2, node1, node2, difference, depth)
    return result


def make_diff(file1, file2):
    input1 = parse_file(file1)
    input2 = parse_file(file2)
    return difference(input1, input2)


def generate_diff(file1, file2, format: str = 'stylish'):
    result = make_diff(file1, file2)
    match format:
        case 'stylish': return stylish(result)
        case 'plain': return plain(result)
        case 'json': return json.dumps(result, indent=2)
        case _: return stylish(result)


def main():
    arguments = parse_args()
    file1 = arguments.first_file
    file2 = arguments.second_file
    format = arguments.format
    print(generate_diff(file1, file2, format))


if __name__ == '__main__':
    main()
