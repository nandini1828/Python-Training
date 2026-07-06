"""
Unit tests for if_else utilities.
"""

import pytest

from if_else.utils import (
    calculate_discount,
    calculate_grade,
    can_vote,
    check_leap_year,
    check_number,
    employee_bonus,
    even_or_odd,
    is_adult,
    largest_number,
    pass_or_fail,
    smallest_number,
    traffic_signal,
    validate_login,
    weather_advice,
)


def test_is_adult():
    assert is_adult(18) is True
    assert is_adult(17) is False


def test_can_vote():
    assert can_vote(21) is True
    assert can_vote(15) is False


def test_calculate_grade():
    assert calculate_grade(95) == "A"
    assert calculate_grade(82) == "B"
    assert calculate_grade(72) == "C"
    assert calculate_grade(65) == "D"
    assert calculate_grade(30) == "F"


def test_largest_number():
    assert largest_number(10, 20) == 20
    assert largest_number(50, 5) == 50


def test_smallest_number():
    assert smallest_number(10, 20) == 10
    assert smallest_number(50, 5) == 5


def test_check_leap_year():
    assert check_leap_year(2024) is True
    assert check_leap_year(2023) is False


def test_validate_login():
    assert validate_login("admin", "python") is True
    assert validate_login("admin", "wrong") is False


def test_calculate_discount():
    assert calculate_discount(6000) == 600
    assert calculate_discount(2000) == 0


def test_employee_bonus():
    assert employee_bonus(5) == 50000
    assert employee_bonus(3) == 10000


def test_traffic_signal():
    assert traffic_signal("red") == "Stop"
    assert traffic_signal("yellow") == "Ready"
    assert traffic_signal("green") == "Go"


def test_weather_advice():
    assert weather_advice("rainy") == "Carry an Umbrella"
    assert weather_advice("sunny") == "Wear Sunglasses"


def test_check_number():
    assert check_number(10) == "Positive"
    assert check_number(-10) == "Negative"
    assert check_number(0) == "Zero"


def test_even_or_odd():
    assert even_or_odd(4) == "Even"
    assert even_or_odd(5) == "Odd"


def test_pass_or_fail():
    assert pass_or_fail(80) == "Pass"
    assert pass_or_fail(20) == "Fail"