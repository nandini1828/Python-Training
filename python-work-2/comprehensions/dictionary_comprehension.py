"""
Dictionary Comprehension.
"""


def demo():

    squares = {
        x: x ** 2
        for x in range(6)
    }

    print(squares)