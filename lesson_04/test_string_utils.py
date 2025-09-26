import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# capitalize - позитивные
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("sky pro", "Sky pro")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# capitalize - негативные
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("123skypro", "123skypro")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# trim - позитивные
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


# trim - негативные
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("  skypro  ", "skypro  ")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# contains - позитивные
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True)
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# contains - негативные
@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "A", False),
    ("SkyPro", "s", False)
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# delete_symbol - позитивные
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", "kyPro"),
    ("SkyPro", "k", "SyPro")
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


# delete_symbol - негативные
@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "x", "SkyPro"),
    ("SkyPro", "s", "SkyPro")
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
