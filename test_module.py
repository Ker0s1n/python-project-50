#!/usr/bin/env python3
from gendiff.scripts.gendiff import generate_diff


diff = generate_diff(
    'tests/fixtures/one.json',
    'tests/fixtures/three.json'
)
print(diff)
