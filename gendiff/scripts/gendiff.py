#!/usr/bin/env python3
import argparse
from gendiff.scripts.instruments import make_diff
from gendiff.scripts.stylish import stylish
from gendiff.scripts.plain import plain
from gendiff.scripts.to_json import to_json


def generate_diff(file1, file2, format: str = 'stylish'):
    result = make_diff(file1, file2)
    match format:
        case 'stylish': return stylish(result)
        case 'plain': return plain(result)
        case 'json': return to_json(result)
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
