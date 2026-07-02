from control_flow.logical_operators import (
    is_eligible,
    can_access,
    is_not_logged_in,
)


def test_is_eligible():
    assert is_eligible(20, True) is True


def test_is_not_eligible():
    assert is_eligible(16, True) is False


def test_can_access():
    assert can_access(False, True) is True


def test_not_logged_in():
    assert is_not_logged_in(False) is True