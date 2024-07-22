#!/usr/bin/env python3
from gendiff.tools.exceptions import exception_format_json


def make_value_for_json(
        key, val, function, deep_indent_size, deep_indent):
    return f'\n{deep_indent}\"{key}\": \
{function(val, deep_indent_size)}'


def del_last_elem(list_for_string):
    if list_for_string[-1] == ',':
        list_for_string.pop()


def json(node, depth: int = 0, replacer: str = ' ', spaces_count: int = 2):
    if not isinstance(node, dict):
        return str(node)

    deep_indent_size = depth + spaces_count
    deep_indent = replacer * deep_indent_size

    result = ['{']
    for key, val in node.items():
        if isinstance(val, dict):
            result.extend(
                make_value_for_json(
                    key, val, json, deep_indent_size, deep_indent))
        else:
            result.append(f'\n{deep_indent}\"{key}\": \
{json(exception_format_json(val), deep_indent_size)}')
            result.append(',')
    del_last_elem(result)
    result.append(f'\n{replacer * depth}' + '},')
    return ''.join(result)
