import pytest
from gendiff.scripts.gendiff import generate_diff, main
from gendiff.scripts.file_parser import parse_file, main as parser_main


@pytest.fixture
def paths():
    return {
        'first_file': 'tests/fixtures/one.json',
        'second_file': 'tests/fixtures/two.json',
        'third_file': 'tests/fixtures/three.json',
        'fourth_file': 'tests/fixtures/one.yaml',
        'fifth_file': 'tests/fixtures/two.yaml',
        'sixth_file': 'tests/fixtures/three.yaml',
        'first_result': 'tests/fixtures/result_1.txt',
        'second_result': 'tests/fixtures/result.txt',
        'third_result': 'tests/fixtures/result_main.txt'
    }


def test_gendiff_main(paths):
    assert main(
        [paths['second_file'], paths['third_file']]
    ) == open(paths['third_result']).read()

    assert main(
        [paths['fifth_file'], paths['sixth_file']]
    ) == open(paths['third_result']).read()


def test_gendiff_merge_json(paths):
    assert generate_diff(
        paths['first_file'],
        paths['second_file']
    ) == open(paths['first_result']).read()

    assert generate_diff(
        paths['first_file'],
        paths['third_file']
    ) == open(paths['second_result']).read()


def test_gendiff_merge_yaml(paths):
    assert generate_diff(
        paths['fourth_file'],
        paths['fifth_file']
    ) == open(paths['first_result']).read()

    assert generate_diff(
        paths['fourth_file'],
        paths['sixth_file']
    ) == open(paths['second_result']).read()


def test_exception_type_of_file(paths):
    assert parse_file(
        paths['second_result']
    ) == {'Exception': 'file has wrong format'}


def test_file_parser_main(paths):
    assert parser_main(
        [paths['first_file']]
    ) == print(parse_file(paths['first_file']))
