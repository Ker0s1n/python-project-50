import pytest
from gendiff.scripts.gendiff import generate_diff, main


@pytest.fixture
def paths():
    return {
        'first_file': 'tests/fixtures/one.json',
        'second_file': 'tests/fixtures/two.json',
        'third_file': 'tests/fixtures/three.json',
        'first_result': 'tests/fixtures/result_1.txt',
        'second_result': 'tests/fixtures/result.txt',
        'third_result': 'tests/fixtures/result_main.txt'
    }


def test_correct_merge(paths):
    assert generate_diff(
        paths['first_file'],
        paths['second_file']
    ) == open(paths['first_result']).read()

    assert generate_diff(
        paths['first_file'],
        paths['third_file']
    ) == open(paths['second_result']).read()


def test_main(paths):
    assert main(
        [paths['second_file'], paths['third_file']]
    ) == open(paths['third_result']).read()
