#!/usr/bin/env python3
from gendiff.scripts.instruments import is_dict, exception_format_json


def make_json_value(
        key, val, function, deep_indent_size, deep_indent):
    return f'\n{deep_indent}\"{key}\": \
{function(val, deep_indent_size)}'


def to_json(value, replacer: str = ' ', spaces_count: int = 2):

    def walk(node, depth: int = 0):
        if not is_dict(node):
            return str(node)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth

        result = ['{']
        for key, val in node.items():
            if is_dict(val):
                result.extend(
                    make_json_value(
                        key, val, walk, deep_indent_size, deep_indent))
            else:
                result.append(f'\n{deep_indent}\"{key}\": \
{walk(exception_format_json(val), deep_indent_size)}')
                result.append(',')
        if result[-1] == ',':
            result.pop()
        result.append(f'\n{current_indent}' + '}')
        return ''.join(result)
    return walk(value)
