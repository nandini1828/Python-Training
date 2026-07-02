from iteration_helpers.any_all import (
    check_any,
    check_all,
)


def test_any_true():
    assert check_any([0, False, 5]) is True


def test_any_false():
    assert check_any([0, False, None]) is False


def test_all_true():
    assert check_all([2, 4, 6]) is True


def test_all_false():
    assert check_all([2, 3, 6]) is False