from iterators_generators.iterator_protocol import (
    create_iterator,
    get_next_item,
)


def test_create_iterator():

    iterator = create_iterator([10, 20, 30])

    assert iter(iterator) is iterator


def test_get_next_item():

    iterator = create_iterator([10, 20, 30])

    assert get_next_item(iterator) == 10
    assert get_next_item(iterator) == 20
    assert get_next_item(iterator) == 30