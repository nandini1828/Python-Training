"""
Short circuit evaluation.
"""


def expensive():

    print("Expensive function executed")
    return True


def demo():

    print("AND Example")

    False and expensive()

    print("\nOR Example")

    True or expensive()