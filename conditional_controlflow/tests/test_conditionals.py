import pytest

from control_flow.conditionals import (
    verify_card,
    pin_verification,
    account_status,
)


def test_verify_card():
    assert verify_card(True) is True
    assert verify_card(False) is False


def test_pin_verification():
    assert pin_verification(1234, 1234) is True
    assert pin_verification(1111, 1234) is False


@pytest.mark.parametrize(
    "balance,expected",
    [
        (15000, "Premium Account"),
        (7000, "Standard Account"),
        (500, "Low Balance Account"),
        (0, "Zero Balance Account"),
    ],
)
def test_account_status(balance, expected):
    assert account_status(balance) == expected