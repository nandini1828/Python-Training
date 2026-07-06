"""
Demo Program for Composition
"""

from composition.composition_example import Computer


def main():
    """
    Driver Function
    """

    desktop = Computer()

    desktop.boot()


if __name__ == "__main__":
    main()