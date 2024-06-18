import argparse

parser = argparse.ArgumentParser(
    description="Compares two configuration files and shows a difference.")
parser.add_argument('first_file')
parser.add_argument('second_file')

def main():
    parser.print_help()


if __name__ == '__main__':
    main()
