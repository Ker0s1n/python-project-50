#!/usr/bin/env python3
from gendiff.scripts.gendiff import generate_diff, parse_args

diff = generate_diff(
    'tests/fixtures/one.json',
    'tests/fixtures/three.json'
)
print(diff)


print(parse_args(['file1.json', 'file2.json']).first_file)
