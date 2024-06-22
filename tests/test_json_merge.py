from gendiff.scripts.gendiff import generate_diff


def test_correct_merge():
    assert generate_diff(
        'tests/fixtures/one.json',
        'tests/fixtures/two.json'
    ) == open('tests/fixtures/result_1.txt').read()


def test_incorrect_merge():
    assert generate_diff(
        'tests/fixtures/one.json',
        'tests/fixtures/three.json'
    ) == open('tests/fixtures/result.txt').read()
