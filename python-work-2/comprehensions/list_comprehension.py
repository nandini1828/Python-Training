"""
List Comprehension.
"""


def demo():

    numbers = list(range(10))

    squares = [x ** 2 for x in numbers]

    evens = [x for x in numbers if x % 2 == 0]

    print(squares)
    print(evens)