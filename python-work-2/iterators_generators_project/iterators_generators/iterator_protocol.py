"""
Iterator Protocol.
"""

def create_iterator(iterable):

    return iter(iterable)


def get_next_item(iterator):

    return next(iterator)



def demo():

    numbers = [10, 20, 30]

    iterator = iter(numbers)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))