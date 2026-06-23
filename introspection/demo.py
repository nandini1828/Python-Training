"""
Demo Program for Introspection
"""

from introspection_utils import inspect_object


def main():
    """
    Driver function.
    """

    name = "Nandini"
    numbers = [1, 2, 3, 4]
    age = 21

    inspect_object(name)
    inspect_object(numbers)
    inspect_object(age)


if __name__ == "__main__":
    main()