"""
zip and zip_longest
"""

from itertools import zip_longest


def demo():

    names = ["Alice", "Bob", "Charlie"]

    marks = [90, 85, 78]

    for name, mark in zip(names, marks):
        print(name, mark)

    print()

    cities = ["Delhi"]

    for item in zip_longest(names, cities, fillvalue="N/A"):
        print(item)