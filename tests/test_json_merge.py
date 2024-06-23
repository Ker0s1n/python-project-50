from gendiff.scripts.gendiff import generate_diff, main


def test_correct_merge():
    assert generate_diff(
        'tests/fixtures/one.json',
        'tests/fixtures/two.json'
    ) == open('tests/fixtures/result_1.txt').read()

    assert generate_diff(
        'tests/fixtures/one.json',
        'tests/fixtures/three.json'
    ) == open('tests/fixtures/result.txt').read()


def test_main():
    assert main(
        ['file1.json', 'file2.json']
    ) == open('tests/fixtures/result_main.txt').read()
