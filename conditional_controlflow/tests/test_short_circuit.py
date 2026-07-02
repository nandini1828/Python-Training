from control_flow.short_circuit import (
    verify_card,
    verify_pin,
    check_balance,
)


def test_verify_card():
    assert verify_card(True) is True
    assert verify_card(False) is False


def test_verify_pin():
    assert verify_pin(1234) is True
    assert verify_pin(9999) is False


def test_check_balance():
    assert check_balance(10000, 2000) is True
    assert check_balance(1000, 5000) is False