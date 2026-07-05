from modules.conditional_project.conditions.match_case import *


def test_day():
    assert day_name(1) == "Monday"


def test_invalid_day():
    assert day_name(20) == "Invalid Day"


def test_add():
    assert calculator(5, 3, "+") == 8


def test_subtract():
    assert calculator(8, 3, "-") == 5


def test_multiply():
    assert calculator(4, 5, "*") == 20


def test_divide():
    assert calculator(10, 2, "/") == 5


def test_division_zero():
    assert calculator(10, 0, "/") == "Division by Zero"


def test_invalid_operator():
    assert calculator(2, 3, "%") == "Invalid Operator"


def test_signal():
    assert traffic_signal("Green") == "Go"


def test_unknown_signal():
    assert traffic_signal("Blue") == "Unknown Signal"