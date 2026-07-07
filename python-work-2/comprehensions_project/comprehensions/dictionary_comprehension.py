"""
Dictionary Comprehension.
"""


def create_square_dictionary(n):
    return {x: x ** 2 for x in range(n)}


def demo():
    squares = {
        x: x ** 2
        for x in range(6)
    }

    print(squares)


if __name__ == "__main__":
    demo()