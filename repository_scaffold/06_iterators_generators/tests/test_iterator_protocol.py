from iterator_protocol.utils import (
    CountDown,
    collect_iterator,
    get_first,
    is_iterable,
    manual_next,
)


def test_iterator_protocol_helpers():
    counter = CountDown(2)
    assert get_first(counter) == 2
    assert collect_iterator(CountDown(2)) == [2, 1, 0]
    assert is_iterable([1, 2])
    assert is_iterable(42) is False

    values = iter([10])
    assert manual_next(values) == 10
    assert manual_next(values, 'done') == 'done'

    try:
        CountDown(-1)
    except ValueError as error:
        assert str(error) == 'start must be zero or greater'
    else:
        raise AssertionError('CountDown should reject negative starts')
