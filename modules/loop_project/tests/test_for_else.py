from modules.loop_project.loops.for_else import *


def test_search_employee_found():
    assert search_employee(["Alice", "Bob"], "Bob") == "Bob found"


def test_search_employee_not_found():
    assert search_employee(["Alice"], "John") == "John not found"


def test_search_policy():
    assert search_policy([101, 102], 102) == "Policy exists"


def test_search_policy_not_found():
    assert search_policy([101], 200) == "Policy not found"


def test_prime_true():
    assert find_prime(13)


def test_prime_false():
    assert not find_prime(12)


def test_locate_product():
    assert locate_product(["Laptop", "Phone"], "Phone")


def test_locate_product_false():
    assert not locate_product(["Laptop"], "TV")