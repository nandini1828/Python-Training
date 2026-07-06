from collections.abc import Iterator

from generators.utils import batched, fibonacci, filtered_numbers, file_lines, natural_numbers


def test_generators_helpers():
    assert list(natural_numbers(3)) == [0, 1, 2]
    assert list(fibonacci(4)) == [0, 1, 1, 2]
    assert list(filtered_numbers([1, 5, 2], 3)) == [5]
    assert list(file_lines(['a\n', 'b'])) == ['a', 'b']
    assert list(batched([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    assert isinstance(fibonacci(1), Iterator)

    try:
        list(batched([1, 2], 0))
    except ValueError as error:
        assert str(error) == 'size must be greater than zero'
    else:
        raise AssertionError('batched should reject size <= 0')
