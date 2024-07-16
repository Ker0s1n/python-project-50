#!/usr/bin/env python3
from gendiff.tools.predicate_funcs import is_dict
from gendiff.tools.exceptions import exception_format_plain


def make_value_for_difference(
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


def make_value_for_stylish(
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


def make_value_for_plain(key, val, function):
    string = []
    match val.get('type'):
        case 'added':
            add = val.get("value")
            if is_dict(add):
                string.append(f"Property \'{key}\' was added \
with value: [complex value]")
            else:
                string.append(f'Property \'{key}\' was added \
with value: {exception_format_plain(function(add))}')
        case 'deleted':
            string.append(f'Property \'{key}\' was removed')
        case 'nested': string.append(function(val.get('value'), key))
        case 'changed':
            value1 = val.get("old_value")
            value2 = val.get("new_value")
            if is_dict(value1):
                value1 = function(val.get("old_value"))
            if is_dict(value2):
                value2 = function(val.get("new_value"))
            string.append(f'Property \'{key}\' was updated. \
From {exception_format_plain(value1)} to {exception_format_plain(value2)}')
    return string


def make_value_for_json(
        key, val, function, deep_indent_size, deep_indent):
    return f'\n{deep_indent}\"{key}\": \
{function(val, deep_indent_size)}'
