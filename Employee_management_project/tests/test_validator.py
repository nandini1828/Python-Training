from utils.validators import is_non_empty_string


def test_is_non_empty_string():
    assert is_non_empty_string("Alice") is True
    assert is_non_empty_string("") is False
