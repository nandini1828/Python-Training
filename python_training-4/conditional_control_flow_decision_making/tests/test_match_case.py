from match_case import display_status


class Dummy:

    order_status = "DELIVERED"


def test_status():

    assert display_status(Dummy()) == "Order Delivered."