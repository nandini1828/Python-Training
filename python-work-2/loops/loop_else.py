"""
for-else and while-else
"""


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