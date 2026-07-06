"""
Unit tests for logical_operators utilities.
"""

from logical_operators.utils import *


def test_can_vote():
    assert can_vote(20, True)
    assert not can_vote(17, True)


def test_login():
    assert validate_login("admin", "python", "admin", "python")
    assert not validate_login("admin", "123", "admin", "python")


def test_access():
    assert has_access(True, False)
    assert has_access(False, True)
    assert not has_access(False, False)


def test_drive():
    assert can_drive(20, True)
    assert not can_drive(15, True)


def test_discount():
    assert should_apply_discount(True, 1000)
    assert should_apply_discount(False, 6000)
    assert not should_apply_discount(False, 1000)


def test_withdraw():
    assert can_withdraw(1000, 500)
    assert not can_withdraw(1000, 1500)


def test_login_needed():
    assert needs_login(False)
    assert not needs_login(True)