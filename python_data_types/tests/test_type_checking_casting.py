from type_checking_casting import (
    check_type,
    strict_type_check,
    safe_cast
)


def test_check_type():
    assert check_type(10, int) is True
    assert check_type("10", int) is False


def test_strict_type_check():
    class A: pass
    class B(A): pass

    assert strict_type_check(B(), A) is True
    assert strict_type_check(B(), B) is True


def test_safe_cast_success():
    assert safe_cast("10", int) == 10
    assert safe_cast("10.5", float) == 10.5


def test_safe_cast_failure():
    assert safe_cast("abc", int) is None
    assert safe_cast("abc", int, 0) == 0