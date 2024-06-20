#!/usr/bin/env python3
import argparse
import json


def generate_diff(file1, file2):
    input1 = json.load(open(file1))
    input2 = json.load(open(file2))
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


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
