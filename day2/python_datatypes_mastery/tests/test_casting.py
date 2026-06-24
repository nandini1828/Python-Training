from primitives import SafeCaster


def test_valid_int_cast():
    assert SafeCaster.cast("123", int) == 123


def test_valid_float_cast():
    assert SafeCaster.cast("12.5", float) == 12.5


def test_invalid_cast_returns_default():
    assert SafeCaster.cast("abc", int, 0) == 0


def test_invalid_cast_returns_none():
    assert SafeCaster.cast("abc", int) is None