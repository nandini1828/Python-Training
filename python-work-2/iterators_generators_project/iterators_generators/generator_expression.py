"""
Generator Expressions.
"""


def demo():

    generator = (
        x ** 2
        for x in range(10)
    )

    for value in generator:
        print(value)