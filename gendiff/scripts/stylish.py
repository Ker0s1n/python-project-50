#!/usr/bin/env python3
from gendiff.scripts.instruments import is_dict


def make_stylish_value(
        key, val, function, deep_indent_size, deep_indent):
    string = []
    match val.get('type'):
        case 'unchanged':
            indent = '  '
            string.append(
                f'\n{deep_indent}{indent}{key}: \
{function(val["value"], deep_indent_size)}')
        case 'changed':
            indent = '- '
            string.append(f'\n{deep_indent}{indent}{key}: \
{function(val["old_value"], deep_indent_size)}')
            indent = '+ '
            string.append(f'\n{deep_indent}{indent}{key}: \
{function(val["new_value"], deep_indent_size)}')
        case 'nested':
            indent = '  '
            string.append(f'\n{deep_indent}{indent}{key}: \
{function(val["value"], deep_indent_size)}')
        case 'deleted':
            indent = '- '
            string.append(f'\n{deep_indent}{indent}{key}: \
{function(val["value"], deep_indent_size)}')
        case 'added':
            indent = '+ '
            string.append(f'\n{deep_indent}{indent}{key}: \
{function(val["value"], deep_indent_size)}')
        case None:
            indent = '  '
            string.append(f'\n{deep_indent}{indent}{key}: \
{function(val, deep_indent_size)}')
    return string


def stylish(value, replacer: str = ' ', spaces_count: int = 4):

    def walk(node, depth: int = 0):
        if not is_dict(node):
            return str(node)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * (deep_indent_size - 2)
        current_indent = replacer * depth

        result = ['{']
        for key, val in node.items():
            if is_dict(val):
                result.extend(
                    make_stylish_value(
                        key, val, walk, deep_indent_size, deep_indent))
            else:
                indent = '  '
                result.append(f'\n{deep_indent}{indent}{key}: \
{walk(val, deep_indent_size)}')
        result.append(f'\n{current_indent}' + '}')
        return ''.join(result)
    return walk(value)
