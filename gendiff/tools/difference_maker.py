#!/usr/bin/env python3
from gendiff.tools.file_parser import parse_file
from gendiff.tools.exceptions import exception_format_difference
from gendiff.tools.value_maker import make_value_for_difference


def difference(node1, node2, depth: int = 0):
    result = {}
    for key in sorted(node1.keys() | node2.keys()):
        value1 = exception_format_difference(node1.get(key))
        value2 = exception_format_difference(node2.get(key))
        result[key] = make_value_for_difference(
            key, value1, value2, node1, node2, difference, depth)
    return result


def make_diff(file1, file2):
    input1 = parse_file(file1)
    input2 = parse_file(file2)
    return difference(input1, input2)
