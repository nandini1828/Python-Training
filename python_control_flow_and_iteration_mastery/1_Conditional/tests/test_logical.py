"""
Tests for logical_operators.py
"""

from conditionals import LogicalOperatorExamples


def test_can_vote():
    assert LogicalOperatorExamples.can_vote(
        20,
        True
    )


def test_login():
    assert LogicalOperatorExamples.login(
        "admin",
        "admin123"
    )


def test_has_access():
    assert LogicalOperatorExamples.has_access(
        False,
        True
    )


def test_email():
    assert LogicalOperatorExamples.validate_email(
        "abc@gmail.com"
    )


def test_even_positive():
    assert LogicalOperatorExamples.is_even_positive(
        20
    )


def test_student_pass():
    assert LogicalOperatorExamples.student_passed(
        50,
        60
    )


def test_account_active():
    assert LogicalOperatorExamples.account_active(
        False
    )