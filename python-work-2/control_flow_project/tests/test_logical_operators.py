from control_flow.logical_operators import (
    is_eligible,
    can_access,
    is_not_logged_in,
)


def test_is_eligible_true():
    assert is_eligible(20, True) is True


def test_is_eligible_false():
    assert is_eligible(16, True) is False


def test_can_access_admin():
    assert can_access(True, False) is True


def test_can_access_permission():
    assert can_access(False, True) is True


def test_can_access_false():
    assert can_access(False, False) is False


def test_not_logged_in():
    assert is_not_logged_in(False) is True
    assert is_not_logged_in(True) is False