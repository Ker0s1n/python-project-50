import pytest
from gendiff.generate_difference import generate_diff
from gendiff.file_parser import parse_file
from gendiff.formatters.plain import exception_format_plain


@pytest.mark.parametrize(
    "path_to_first_file, path_to_second_file, format, result",
    [
        ('tests/fixtures/misha_profile_20_years_old.json',
         'tests/fixtures/misha_profile_30_years_old.json',
         'stylish',
         'tests/fixtures/20_30_yo_misha_profile_comparison.txt'
         ),
        ('tests/fixtures/misha_profile_20_years_old.json',
         'tests/fixtures/misha_profile_40_years_old.json',
         'stylish',
         'tests/fixtures/20_40_yo_misha_profile_comparison.txt'
         ),
        ('tests/fixtures/data_for_test_before.json',
         'tests/fixtures/data_for_test_after.json',
         'plain',
         'tests/fixtures/plain_difference_for_test_data.txt'
         ),
        ('tests/fixtures/misha_profile_30_years_old.yaml',
         'tests/fixtures/misha_profile_40_years_old.yaml',
         'jhkhkkjkj',
         'tests/fixtures/30_40_yo_misha_profile_comparison.txt'
         ),
        ('tests/fixtures/data_for_test_before.yaml',
         'tests/fixtures/data_for_test_after.yaml',
         'stylish',
         'tests/fixtures/stylish_difference_for_test_data.txt'
         ),
        ('tests/fixtures/data_for_test_before.json',
         'tests/fixtures/data_for_test_after.json',
         'json',
         'tests/fixtures/json_difference_for_test_data.txt'
         ),
    ]
)
def test_diff_and_format(
    path_to_first_file,
    path_to_second_file,
    format,
    result
):
    assert generate_diff(
        path_to_first_file,
        path_to_second_file,
        format
    ) == open(result).read()


def test_exception_type_of_file():
    assert parse_file(
        'tests/fixtures/json_difference_for_test_data.txt'
    ) == {'Exception': 'file has wrong format'}


def test_exception_format():
    for value in ['50', [True], 'text',]:
        assert exception_format_plain(value) == f"'{str(value)}'"
    assert exception_format_plain(True) == 'true'
    assert exception_format_plain(False) == 'false'
    assert exception_format_plain(None) == 'null'
    assert exception_format_plain(50) == 50
    assert exception_format_plain('[complex value]') == '[complex value]'
