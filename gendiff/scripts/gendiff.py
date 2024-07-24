#!/usr/bin/env python3
from gendiff.argument_parser import parse_args
from gendiff.generate_difference import generate_diff


def main():
    """
    Returns the difference between two files in the specified format
    according to the arguments passed.
    """
    arguments = parse_args()
    file1 = arguments.first_file
    file2 = arguments.second_file
    format = arguments.format
    print(generate_diff(file1, file2, format))


if __name__ == '__main__':
    main()
