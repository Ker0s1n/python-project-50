#!/usr/bin/env python3
import argparse
from gendiff.tools.difference_maker import make_diff
from gendiff.formatters.stylish_formatter import stylish
from gendiff.formatters.plain_formatter import plain
from gendiff.formatters.json_formatter import json


def generate_diff(file1, file2, format: str = 'stylish'):
    result = make_diff(file1, file2)
    match format:
        case 'stylish': return stylish(result)
        case 'plain': return plain(result)
        case 'json': return json(result)[:-1]
        case _: return stylish(result)


def parse_args(arg_list: list[str] | None):
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output (default: stylish)'
    )
    return parser.parse_args(arg_list)


def main(arg_list: list[str] | None = None):
    file1 = parse_args(arg_list).first_file
    file2 = parse_args(arg_list).second_file
    format = parse_args(arg_list).format
    print(generate_diff(file1, file2, format))


if __name__ == '__main__':
    main()
