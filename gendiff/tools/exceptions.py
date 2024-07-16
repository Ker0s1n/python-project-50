#!/usr/bin/env python3
def exception_format_difference(value):
    match value:
        case None: return 'null'
        case False: return 'false'
        case True: return 'true'
        case _: return value


def exception_format_plain(value):
    if value in ['true', 'false', 'null', '[complex value]']:
        return value
    elif type(value) is int:
        return value
    else:
        return f"'{str(value)}'"


def exception_format_json(value):
    if value in ['true', 'false', 'null']:
        return value
    elif type(value) is int:
        return value
    else:
        return f'"{str(value)}"'
