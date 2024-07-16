#!/usr/bin/env python3
from gendiff.tools.predicate_funcs import is_dict
from gendiff.tools.exceptions import exception_format_plain
from gendiff.tools.value_maker import make_value_for_plain


def make_path(parent, child):
    if parent:
        return f'{parent}.{child}'
    return child


def plain(node, parent_key: str = ''):
    if not is_dict(node):
        return str(node)

    result = []
    for key, val in node.items():
        key = make_path(parent_key, key)
        if is_dict(val):
            result.extend(make_value_for_plain(key, val, plain))
        else:
            result.append(exception_format_plain('[complex value]'))
    return '\n'.join(result)
