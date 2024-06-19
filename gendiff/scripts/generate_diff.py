#!/usr/bin/env python3
import json


def generate_diff(file1, file2):
    input1 = json.load(open(file1))
    input2 = json.load(open(file2))
    keys = sorted(list(set(
        list(input1.keys()) + list(input2.keys())
    )))
    stack = ['{']
    for key in keys:
        try:
            value1 = input1[key]
        except Exception:
            value1 = 'error'
        try:
            value2 = input2[key]
        except Exception:
            value2 = 'error'
        if value1 == value2 and value1 != 'error':
            stack.append(f'    {key}: {value1}')
        elif value1 != value2 and value1 != 'error':
            stack.append(f'  - {key}: {value1}')
            if value2 != 'error':
                stack.append(f'  + {key}: {value2}')
        else:
            stack.append(f'  + {key}: {value2}')
    stack.append('}')
    return '\n'.join(stack).lower()


def main():
    generate_diff()


if __name__ == '__main__':
    main()
