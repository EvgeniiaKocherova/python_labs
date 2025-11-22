import pytest
import sys

sys.path.append("../src/lib")
from text import *


@pytest.mark.parametrize(
    "source,expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("   ", ""),
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
        ("  двойные   пробелы  ", ["двойные", "пробелы"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        (["bb", "aa", "bb", "aa", "cc"], {"aa": 2, "bb": 2, "cc": 1}),
        (["bb"], {"bb": 1}),
        ([], {}),
    ],
)
def test_count_freq_and_top_n(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),
        ({"aa": 2, "bb": 2, "cc": 1}, 2, [("aa", 2), ("bb", 2)]),
        ({"aa": 2, "bb": 2, "cc": 1}, 0, []),
        ({"aa": 2, "bb": 2, "cc": 1}, 1, [("aa", 2)]),
        ({"aa": 2, "bb": 2, "cc": 1}, 10, [("aa", 2), ("bb", 2), ("cc", 1)]),
    ],
)
def test_top_n(freq, n, expected):
    assert top_n(freq, n) == expected
