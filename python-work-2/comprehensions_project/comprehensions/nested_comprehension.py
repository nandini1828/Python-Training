"""
Nested Comprehensions.
"""


def flatten_matrix(matrix):
    return [
        item
        for row in matrix
        for item in row
    ]


def create_grid(rows, cols):
    return [
        [0 for _ in range(cols)]
        for _ in range(rows)
    ]


def flatten_demo():
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6],
    ]

    flattened = flatten_matrix(matrix)

    print(flattened)


def grid_demo():
    grid = create_grid(4, 3)

    print(grid)


def demo():
    flatten_demo()
    grid_demo()


if __name__ == "__main__":
    demo()