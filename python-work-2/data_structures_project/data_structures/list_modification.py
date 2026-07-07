"""
Modifying list while iterating.
"""

def remove_even_numbers(numbers):

    return [num for num in numbers if num % 2 != 0]



def incorrect_way():

    print("Incorrect Way")

    numbers = [2, 4, 6, 7, 8]

    for num in numbers:

        if num % 2 == 0:
            numbers.remove(num)

    print(numbers)


def correct_way_copy():

    print("\nCorrect Way (Copy)")

    numbers = [2, 4, 6, 7, 8]

    for num in numbers[:]:

        if num % 2 == 0:
            numbers.remove(num)

    print(numbers)


def correct_way_comprehension():

    print("\nCorrect Way (Comprehension)")

    numbers = [2, 4, 6, 7, 8]

    numbers = [num for num in numbers if num % 2 != 0]

    print(numbers)


def demo():

    incorrect_way()
    correct_way_copy()
    correct_way_comprehension()