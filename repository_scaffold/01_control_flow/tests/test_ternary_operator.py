"""
Unit tests for ternary_operator utilities.
"""

from ternary_operator.utils import (
    adult_status,
    employee_bonus,
    even_or_odd,
    larger,
    login_message,
    pass_fail,
    positive_negative,
    scholarship_status,
    smaller,
    weather_message,
)


def test_adult_status():
    assert adult_status(20) == "Adult"
    assert adult_status(15) == "Minor"


def test_even_or_odd():
    assert even_or_odd(4) == "Even"
    assert even_or_odd(5) == "Odd"


def test_larger():
    assert larger(10, 20) == 20


def test_smaller():
    assert smaller(10, 20) == 10


def test_pass_fail():
    assert pass_fail(80) == "Pass"
    assert pass_fail(30) == "Fail"


def test_positive_negative():
    assert positive_negative(10) == "Positive"
    assert positive_negative(-5) == "Negative"


def test_login_message():
    assert login_message(True) == "Welcome"
    assert login_message(False) == "Access Denied"


def test_weather_message():
    assert weather_message(True) == "Stay Inside"
    assert weather_message(False) == "Go Outside"


def test_scholarship_status():
    assert scholarship_status(95) == "Eligible"
    assert scholarship_status(70) == "Not Eligible"


def test_employee_bonus():
    assert employee_bonus(5) == 50000
    assert employee_bonus(3) == 10000