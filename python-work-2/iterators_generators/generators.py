"""
Generators using yield.
"""


def countdown(start):

    while start > 0:
        yield start
        start -= 1


def fibonacci(limit):

    a, b = 0, 1

    for _ in range(limit):
        yield a
        a, b = b, a + b


def demo():

    print("Countdown")

    for value in countdown(5):
        print(value)

    print("\nFibonacci")

    for value in fibonacci(10):
        print(value)