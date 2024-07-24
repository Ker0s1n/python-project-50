import argparse


def parse_args():
    """
    Generates a description of the function and its arguments
    and recognizes the parameters when the function is called.
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output (default: stylish)'
    )
    return parser.parse_args()
