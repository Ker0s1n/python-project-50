from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json_format


def difference_formatter(format):
    match format:
        case 'stylish': return stylish
        case 'plain': return plain
        case 'json': return json_format
        case _: return stylish
