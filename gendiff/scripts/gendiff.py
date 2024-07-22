#!/usr/bin/env python3
import json
from gendiff.difference_maker import make_diff
from gendiff.argument_parser import parse_args
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def generate_diff(file1, file2, format: str = 'stylish'):
    result = make_diff(file1, file2)
    match format:
        case 'stylish': return stylish(result)
        case 'plain': return plain(result)
        case 'json': return json.dumps(result, indent=2)
        case _: return stylish(result)


def main():
    arguments = parse_args()
    file1 = arguments.first_file
    file2 = arguments.second_file
    format = arguments.format
    print(generate_diff(file1, file2, format))


if __name__ == '__main__':
    main()
