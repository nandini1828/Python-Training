from model import Order
from if_elif_else import validate_login


def test_valid_login():

    order = Order(
        "Nandini",
        True,
        ["Pizza"],
        True,
        True,
        False,
        None,
        "PLACED"
    )

    assert validate_login(order) == "Login successful."


def test_empty_cart():

    order = Order(
        "Nandini",
        True,
        [],
        True,
        True,
        False,
        None,
        "PLACED"
    )

    assert validate_login(order) == "Cart is empty."


def test_not_logged_in():

    order = Order(
        "Nandini",
        False,
        ["Pizza"],
        True,
        True,
        False,
        None,
        "PLACED"
    )

    assert validate_login(order) == "Please log in."