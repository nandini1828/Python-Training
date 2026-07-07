from iterators_generators.generator_expressions import generator_expression_example


def test_generator_expression_squares_values():
    squares = generator_expression_example([1, 2, 3, 4])
    assert list(squares) == [1, 4, 9, 16]
