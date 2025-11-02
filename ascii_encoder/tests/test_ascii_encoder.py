import pytest
from ascii_encoder.encoder import text_to_ascii
from ascii_encoder.decoder import ascii_to_text


def test_text_to_ascii_basic():
    assert text_to_ascii("Hello") == "72 101 108 108 111"


def test_ascii_to_text_basic():
    assert ascii_to_text("72 101 108 108 111") == "Hello"


def test_empty_string():
    assert text_to_ascii("") == ""
    assert ascii_to_text("") == ""


def test_invalid_ascii_value():
    with pytest.raises(ValueError):
        ascii_to_text("999")


def test_non_ascii_input():
    with pytest.raises(ValueError):
        text_to_ascii("hello😊")