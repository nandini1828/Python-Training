"""
Lists:
- Indexing
- Slicing
- Iteration
"""


def indexing_demo():

    numbers = [10, 20, 30, 40, 50]

    print("First:", numbers[0])
    print("Last :", numbers[-1])


def slicing_demo():

    numbers = [10, 20, 30, 40, 50]

    print(numbers[1:4])
    print(numbers[:3])
    print(numbers[::2])
    print(numbers[::-1])


def looping_demo():

    fruits = ["Apple", "Banana", "Orange"]

    for fruit in fruits:
        print(fruit)


def demo():

    indexing_demo()
    slicing_demo()
    looping_demo()