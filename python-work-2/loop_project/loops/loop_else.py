"""
for-else and while-else
"""

def search_number(numbers, target):

    for number in numbers:
        if number == target:
            return 'Found'
    return 'Not Found'


def while_search(numbers, target):

    i = 0
    while i < len(numbers):
        if numbers[i] == target:
            return 'Found'
        i += 1
    return 'Not Found'



def search(target):

    numbers = [10, 20, 30, 40]

    for number in numbers:

        if number == target:
            print("Found")
            break

    else:
        print("Not Found")


def demo():

    search(30)

    search(50)