from dunder import Box


def test_add():
    a = Box(10)
    b = Box(5)
    assert (a + b).value == 15


def test_eq():
    assert Box(10) == Box(10)