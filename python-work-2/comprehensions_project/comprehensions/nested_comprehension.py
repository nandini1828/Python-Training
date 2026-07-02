"""
Nested Comprehensions.
"""


def flatten_demo():

    matrix = [
        [1, 2],
        [3, 4],
        [5, 6],
    ]

    flattened = [
        item
        for row in matrix
        for item in row
    ]

    print(flattened)


def grid_demo():

    grid = [
        [0 for _ in range(3)]
        for _ in range(4)
    ]

    print(grid)


def demo():

    flatten_demo()
    grid_demo()