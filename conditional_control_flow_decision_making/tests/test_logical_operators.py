from model import Order
from logical_operators import verify_order


def test_order_valid():

    class Dummy:
        payment_success = True
        address_available = True

    assert verify_order(Dummy()) == "Order can be processed."


def test_order_invalid():

    class Dummy:
        payment_success = False
        address_available = True

    assert verify_order(Dummy()) == "Payment or address validation failed."