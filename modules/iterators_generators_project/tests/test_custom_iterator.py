from generators.custom_iterator import CountDownIterator


def test_custom_iterator():
    iterator = CountDownIterator(3)
    assert list(iterator) == [3, 2, 1, 0]
