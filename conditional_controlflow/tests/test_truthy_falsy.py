from control_flow.truthy_falsy import (
    card_status,
    pin_validation,
)


def test_card_status():
    assert card_status("HDFC") is True
    assert card_status(None) is False


def test_pin_validation():
    assert pin_validation("1234") is True
    assert pin_validation("") is False