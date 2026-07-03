"""Number Generator"""


class CountDownIterator:
    """A simple iterator that counts down from a starting number."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


def fibonacci(limit):
    """Yield Fibonacci numbers up to a limit."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def square_numbers(limit):
    """Yield square numbers up to a limit."""
    for number in range(limit + 1):
        yield number * number


def generator_expression_example(numbers):
    """Return even numbers using a generator expression."""
    return (number for number in numbers if number % 2 == 0)


def compare_lists_and_generators(numbers):
    """Show that a generator uses less memory than a list."""
    list_version = [number * number for number in numbers]
    generator_version = (number * number for number in numbers)
    return list_version, generator_version


def main():
    print("Custom iterator:")
    iterator = CountDownIterator(3)
    for number in iterator:
        print(number)

    print("\nFibonacci numbers:")
    for value in fibonacci(20):
        print(value, end=" ")
    print()

    print("\nSquare numbers:")
    for value in square_numbers(5):
        print(value, end=" ")
    print()

    numbers = [1, 2, 3, 4, 5, 6]
    print("\nEven numbers from generator expression:")
    for value in generator_expression_example(numbers):
        print(value, end=" ")
    print()

    list_version, generator_version = compare_lists_and_generators(numbers)
    print("\nList version:", list_version)
    print("Generator version object:", generator_version)


if __name__ == "__main__":
    main()
