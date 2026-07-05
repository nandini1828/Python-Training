from modules.conditional_project.conditions.short_circuit import *


def test_safe_division():
    assert safe_division(10, 2) is True


def test_zero_division():
    assert safe_division(10, 0) is False


def test_logical_or():
    assert logical_or(True) is True


def test_logical_and():
    assert logical_and(True) is True


def test_logical_and_false():
    assert logical_and(False) is False