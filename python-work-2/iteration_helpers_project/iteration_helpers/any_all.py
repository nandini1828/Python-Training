"""
any() and all()
"""


def demo():

    values = [0, False, "", 5]

    print(any(values))

    print(all(values))

    numbers = [2, 4, 6, 8]

    print(all(num % 2 == 0 for num in numbers))

    print(any(num > 5 for num in numbers))