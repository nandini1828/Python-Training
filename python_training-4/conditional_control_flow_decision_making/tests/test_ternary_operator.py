from ternary_operator import delivery_charge


class Premium:

    premium_member = True


class Normal:

    premium_member = False


def test_premium():

    assert delivery_charge(Premium()) == 0


def test_normal():

    assert delivery_charge(Normal()) == 49