from short_circuit import apply_coupon


class Dummy:

    coupon = {
        "code": "SAVE10",
        "active": True
    }


class EmptyCoupon:

    coupon = None


def test_coupon():

    assert apply_coupon(Dummy()) == "Coupon Applied: SAVE10"


def test_no_coupon():

    assert apply_coupon(EmptyCoupon()) == "No active coupon."