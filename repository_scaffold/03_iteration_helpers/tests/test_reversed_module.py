from reversed_module.utils import *

def test_reverse_list():
    assert reverse_list([1,2,3]) == [3,2,1]


def test_reverse_string():
    assert reverse_string("abc") == "cba"


def test_is_palindrome():
    assert is_palindrome("madam") is True
    assert is_palindrome("hello") is False


def test_reverse_words():
    assert reverse_words("I love Python") == "Python love I"