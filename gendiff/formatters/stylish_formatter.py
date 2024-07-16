#!/usr/bin/env python3
from gendiff.tools.predicate_funcs import is_dict
from gendiff.tools.value_maker import make_value_for_stylish


def stylish(node, depth: int = 0, replacer: str = ' ', spaces_count: int = 4):
    if not is_dict(node):
        return str(node)

    deep_indent_size = depth + spaces_count
    deep_indent = replacer * (deep_indent_size - 2)
    current_indent = replacer * depth

    result = ['{']
    for key, val in node.items():
        if is_dict(val):
            result.extend(
                make_value_for_stylish(
                    key, val, stylish, deep_indent_size, deep_indent))
        else:
            indent = '  '
            result.append(f'\n{deep_indent}{indent}{key}: \
{stylish(val, deep_indent_size)}')
    result.append(f'\n{current_indent}' + '}')
    return ''.join(result)
