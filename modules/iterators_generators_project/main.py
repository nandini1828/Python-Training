"""Entry point for the iterators and generators project."""

from generators.custom_iterator import CountDownIterator
from generators.generator_expressions import square_numbers, even_numbers
from generators.generator_functions import countdown, fibonacci_numbers
from generators.iterator_protocol import IterableCounter, next_value


def main() -> None:
    print("next value:", next_value([10, 20, 30]))
    print("counter:", list(IterableCounter(3)))
    print("countdown:", list(countdown(3)))
    print("fibonacci:", list(fibonacci_numbers(6)))
    print("squares:", list(square_numbers([1, 2, 3, 4])))
    print("evens:", list(even_numbers([1, 2, 3, 4, 5])))
    print("custom iterator:", list(CountDownIterator(3)))


if __name__ == "__main__":
    main()
