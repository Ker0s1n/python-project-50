#!/usr/bin/env python3
from gendiff.scripts.file_parser import parse_file, main as parser_main

diff = parse_file(
    'tests/fixtures/two.yaml'
)
print(diff)


parser_main(['tests/fixtures/two.yaml'])
