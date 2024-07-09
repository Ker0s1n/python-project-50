import pytest
from gendiff.scripts.gendiff import generate_diff, main
from gendiff.scripts.instruments import parse_file


@pytest.fixture
def paths():
    return {
        'first_file': 'tests/fixtures/one.json',
        'second_file': 'tests/fixtures/two.json',
        'third_file': 'tests/fixtures/three.json',
        'fourth_file': 'tests/fixtures/one.yaml',
        'fifth_file': 'tests/fixtures/two.yaml',
        'sixth_file': 'tests/fixtures/three.yaml',
        'seventh_file': 'tests/fixtures/four.yaml',
        'eighth_file': 'tests/fixtures/five.yaml',
        'first_result': 'tests/fixtures/result_1.txt',
        'second_result': 'tests/fixtures/result.txt',
        'third_result': 'tests/fixtures/result_main.txt',
        'fourth_result': 'tests/fixtures/result_nested.txt',
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

    assert generate_diff(
        paths['seventh_file'],
        paths['eighth_file']
    ) == open(paths['fourth_result']).read()


def test_exception_type_of_file(paths):
    assert parse_file(
        paths['second_result']
    ) == {'Exception': 'file has wrong format'}
