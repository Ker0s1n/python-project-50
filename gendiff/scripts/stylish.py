#!/usr/bin/env python3
from gendiff.scripts.instruments import is_dict


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
                if val.get('type') == 'unchanged':
                    indent = '  '
                    result.append(f'\n{deep_indent}{indent}{key}: {walk(val["value"], deep_indent_size)}')
                elif val.get('type') == 'changed':
                    indent = '- '
                    result.append(f'\n{deep_indent}{indent}{key}: {walk(val["old_value"], deep_indent_size)}')
                    indent = '+ '
                    result.append(f'\n{deep_indent}{indent}{key}: {walk(val["new_value"], deep_indent_size)}')
                elif val.get('type') == 'nested':
                    indent = '  '
                    result.append(f'\n{deep_indent}{indent}{key}: {walk(val["value"], deep_indent_size)}')
                elif val.get('type') == 'deleted':
                    indent = '- '
                    result.append(f'\n{deep_indent}{indent}{key}: {walk(val["value"], deep_indent_size)}')
                elif val.get('type') == 'added':
                    indent = '+ '
                    result.append(f'\n{deep_indent}{indent}{key}: {walk(val["value"], deep_indent_size)}')
                elif val.get('type') is None:
                    indent = '  '
                    result.append(f'\n{deep_indent}{indent}{key}: {walk(val, deep_indent_size)}')
            else:
                indent = '  '
                result.append(f'\n{deep_indent}{indent}{key}: {walk(val, deep_indent_size)}')
        result.append(f'\n{current_indent}' + '}')
        return ''.join(result)
    return walk(value)
