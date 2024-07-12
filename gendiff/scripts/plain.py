#!/usr/bin/env python3
from gendiff.scripts.instruments import is_dict, exception_format


def make_path(parent, child):
    if parent:
        return f'{parent}.{child}'
    return child


def get_string(key, val, function):
    string = []
    match val.get('type'):
        case 'added':
            add = val.get("value")
            if is_dict(add):
                string.append(f"Property \'{key}\' was added \
with value: [complex value]")
            else:
                string.append(f'Property \'{key}\' was added \
with value: {exception_format(function(add))}')
        case 'deleted':
            string.append(f'Property \'{key}\' was removed')
        case 'nested': string.append(function(val.get('value'), key))
        case 'changed':
            value1 = function(val.get("old_value"))
            value2 = function(val.get("new_value"))
            string.append(f'Property \'{key}\' was updated. \
From {exception_format(value1)} to {exception_format(value2)}')
    return string


def plain(value):

    def walk(node, parent_key: str = ''):
        if not is_dict(node):
            return str(node)

        result = []
        for key, val in node.items():
            key = make_path(parent_key, key)
            if is_dict(val):
                result.extend(get_string(key, val, walk))
            else:
                result.append(exception_format('[complex value]'))
        return '\n'.join(result)
    return walk(value)
