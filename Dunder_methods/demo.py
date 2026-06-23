"""
Demo Program for Dunder Methods
"""

from dunder_examples import Student


def main():
    """
    Driver function.
    """

    student = Student("Nandini", 21)

    print(student)

    print(repr(student))

    print(len(student))


if __name__ == "__main__":
    main()