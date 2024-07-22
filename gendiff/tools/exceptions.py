#!/usr/bin/env python3
def exception_format_plain(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif value == '[complex value]':
        return value
    elif type(value) is int:
        return value
    else:
        return f"'{str(value)}'"


def exception_format_json(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif type(value) is int:
        return value
    else:
        return f'"{str(value)}"'
