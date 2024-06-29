#!/usr/bin/env python3
import argparse
import yaml
import json


def parse_file(path_to_file: str):
    if '.yml' in path_to_file or '.yaml' in path_to_file:
        with open(path_to_file) as file_to_parse:
            result = yaml.load(file_to_parse, Loader=yaml.FullLoader)
    elif '.json' in path_to_file:
        with open(path_to_file) as file_to_parse:
            result = json.load(file_to_parse)
    else:
        result = {'Exception': 'file has wrong format'}
    return result


def parse_args(arg_list: list[str] | None):
    parser = argparse.ArgumentParser(
        description="displays the contents of files with the extension\
         '.yaml', '.yml', '.json'. Contains the 'parse_file' function,\
         the result of which is a dictionary for use in python")
    parser.add_argument('path_to_file')
    return parser.parse_args(arg_list)


def main(arg_list: list[str] | None = None):
    result = parse_file(parse_args(arg_list).path_to_file)
    print(result)


if __name__ == '__main__':
    main()
