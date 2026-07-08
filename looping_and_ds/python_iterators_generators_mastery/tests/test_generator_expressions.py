from looping_and_ds.python_iterators_generators_mastery.iterators_generators.generator_expressions import (
    build_square_generator,
    build_even_generator,
    build_scaled_generator,
    run_debug_demo,
)


def test_build_square_generator():
    generator = build_square_generator([1, 2, 3, 4])
    assert list(generator) == [1, 4, 9, 16]


def test_build_even_generator():
    generator = build_even_generator([1, 2, 3, 4, 5, 6])
    assert list(generator) == [2, 4, 6]


def test_build_scaled_generator():
    generator = build_scaled_generator([1, 2, 3], factor=2, offset=1)
    assert list(generator) == [3, 5, 7]


def test_run_debug_demo():
    steps, total = run_debug_demo([1, 2, 3], factor=2, offset=1)
    assert steps[0]["adjusted"] == 3
    assert steps[-1]["running_total"] == 15
    assert total == 15