from iterators_generators.iterator_protocol import IteratorExample


def test_iterator_protocol_yields_values_in_order():
    values = IteratorExample([10, 20, 30])
    assert list(values) == [10, 20, 30]
