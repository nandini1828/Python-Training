from control_flow.logical_operators import (
    login,
    cash_withdrawal,
    premium_lounge,
)


def test_login():
    assert login(True, True) is True
    assert login(True, False) is False


def test_cash_withdrawal():
    assert cash_withdrawal(10000, 5000) is True
    assert cash_withdrawal(2000, 5000) is False


def test_premium_lounge():
    assert premium_lounge(True, False) is True
    assert premium_lounge(False, True) is True
    assert premium_lounge(False, False) is False