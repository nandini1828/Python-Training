"""
Set examples.
"""

def contains_number(numbers, value):

    return value in numbers


def unique_values(values):

    return set(values)



def membership_demo():

    numbers = {10, 20, 30, 40}

    print(20 in numbers)
    print(100 in numbers)


def looping_demo():

    colors = {"Red", "Green", "Blue"}

    for color in colors:
        print(color)


def demo():

    membership_demo()
    looping_demo()