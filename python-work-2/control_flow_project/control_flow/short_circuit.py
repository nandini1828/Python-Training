"""
Short circuit evaluation.
"""

def and_short_circuit():

    return False and expensive()


def or_short_circuit():

    return True or expensive()



def expensive():

    print("Expensive function executed")
    return True


def demo():

    print("AND Example")

    False and expensive()

    print("\nOR Example")

    True or expensive()