import pytest
from caesar.cipher import encrypt, decrypt


def test_encrypt_basic():
    assert encrypt("ABC", 3) == "DEF"
    assert encrypt("abc", 1) == "bcd"


def test_decrypt_basic():
    assert decrypt("DEF", 3) == "ABC"


def test_wrap_around():
    assert encrypt("xyz", 3) == "abc"


def test_nonalpha_preserved():
    assert encrypt("Hello, World! 123", 5) == "Mjqqt, Btwqi! 123"


def test_invalid_non_ascii():
    with pytest.raises(ValueError):
        encrypt("hello😊", 3)