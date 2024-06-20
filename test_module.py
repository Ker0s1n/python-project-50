#!/usr/bin/env python3
from gendiff.scripts.gendiff import generate_diff


diff = generate_diff('file1.json', 'file2.json')
print(diff)
