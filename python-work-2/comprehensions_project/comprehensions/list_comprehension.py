"""
List Comprehension.
"""


def create_squares(n):
    return [x ** 2 for x in range(n)]


def get_even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]


def demo():
    numbers = list(range(10))

    squares = [x ** 2 for x in numbers]

    evens = [x for x in numbers if x % 2 == 0]

    print(squares)
    print(evens)


if __name__ == "__main__":
    demo()