"""
Pattern Matching
Python 3.10+
"""


def day(day_no):

    match day_no:

        case 1:
            return "Monday"

        case 2:
            return "Tuesday"

        case 3:
            return "Wednesday"

        case _:
            return "Invalid"


def demo():
    print(day(1))
    print(day(10))