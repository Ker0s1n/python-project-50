from gendiff.difference_maker import make_diff
from gendiff.formatters.__init__ import difference_formatter


def generate_diff(file1, file2, format: str = 'stylish'):
    """Returns the difference between two files in the specified format."""
    result = make_diff(file1, file2)
    return difference_formatter(format)(result)
