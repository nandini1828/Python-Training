"""
Tests for if_else.py
"""

from conditionals import IfElseExamples


def test_positive_number():
    assert IfElseExamples.check_number(10) == "Positive"


def test_negative_number():
    assert IfElseExamples.check_number(-5) == "Negative"


def test_zero():
    assert IfElseExamples.check_number(0) == "Zero"


def test_voting_age():
    assert IfElseExamples.check_age(20) == "Eligible to Vote"


def test_not_voting_age():
    assert IfElseExamples.check_age(15) == "Not Eligible to Vote"


def test_grade():
    assert IfElseExamples.calculate_grade(95) == "A"


def test_even():
    assert IfElseExamples.check_even_or_odd(8) == "Even"


def test_odd():
    assert IfElseExamples.check_even_or_odd(7) == "Odd"


def test_login():
    assert (
        IfElseExamples.login_status(
            "admin",
            "admin123"
        )
        == "Login Successful"
    )