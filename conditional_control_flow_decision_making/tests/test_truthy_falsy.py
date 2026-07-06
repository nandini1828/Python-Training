from model import Order
from truthy_falsy import check_cart


def test_cart_has_items():

    order = Order(
        "Nandini",
        True,
        ["Burger"],
        True,
        True,
        False,
        None,
        "PLACED"
    )

    assert check_cart(order) == "Items available for checkout."


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

    assert check_cart(order) == "No items found."