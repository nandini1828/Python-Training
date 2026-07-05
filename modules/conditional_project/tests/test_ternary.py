from modules.conditional_project.conditions.ternary import *


def test_even():
    assert even_or_odd(8) == "Even"


def test_odd():
    assert even_or_odd(9) == "Odd"


def test_maximum():
    assert maximum(10, 5) == 10


def test_maximum_reverse():
    assert maximum(4, 20) == 20


def test_discount_member():
    assert discount(True) == 20


def test_discount_non_member():
    assert discount(False) == 0


def test_pass():
    assert pass_fail(60) == "Pass"


def test_fail():
    assert pass_fail(20) == "Fail"


def test_adult():
    assert age_category(25) == "Adult"


def test_minor():
    assert age_category(10) == "Minor"