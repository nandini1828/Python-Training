from modules.conditional_project.conditions.truthy import *


def test_cart():
    assert cart_status(["Milk"]) == "Items Available"


def test_empty_cart():
    assert cart_status([]) == "Cart Empty"


def test_username():
    assert username_exists("Indiana") is True


def test_blank_username():
    assert username_exists("") is False


def test_dictionary():
    assert check_dictionary({"id": 1}) == "Dictionary Contains Data"


def test_empty_dictionary():
    assert check_dictionary({}) == "Dictionary Empty"


def test_zero():
    assert number_status(0) == "Zero"


def test_non_zero():
    assert number_status(5) == "Non-zero"


def test_profile():
    assert profile({"name": "John"}) is True


def test_no_profile():
    assert profile({}) is False