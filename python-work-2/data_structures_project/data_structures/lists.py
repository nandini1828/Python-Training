"""
Lists:
- Indexing
- Slicing
- Iteration
"""

def get_first_element(items):

    return items[0]


def get_last_element(items):

    return items[-1]


def slice_list(items, start, end):

    return items[start:end]



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