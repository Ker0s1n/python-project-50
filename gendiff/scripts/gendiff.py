#!/usr/bin/env python3
import argparse
from gendiff.scripts.file_parser import parse_file


def generate_diff(file1, file2):
    input1 = parse_file(file1)
    input2 = parse_file(file2)
    keys = sorted(list(set(
        list(input1.keys()) + list(input2.keys())
    )))
    stack = ['{']
    for key in keys:
        value1 = input1.get(key)
        value2 = input2.get(key)
        if value1 == value2 and value1 is not None:
            stack.append(f'    {key}: {value1}')
        elif value1 != value2 and value1 is not None:
            stack.append(f'  - {key}: {value1}')
            if value2 is not None:
                stack.append(f'  + {key}: {value2}')
        else:
            stack.append(f'  + {key}: {value2}')
    stack.append('}')
    return '\n'.join(stack).lower()


def parse_args(arg_list: list[str] | None):
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args(arg_list)


def main(arg_list: list[str] | None = None):
    file1 = parse_args(arg_list).first_file
    file2 = parse_args(arg_list).second_file
    return generate_diff(file1, file2)


if __name__ == '__main__':
    main()
