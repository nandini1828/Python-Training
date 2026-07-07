"""
Dictionary iteration.
"""

def get_keys(data):

    return data.keys()


def get_values(data):

    return data.values()


def get_items(data):

    return data.items()



def demo():

    student = {
        "name": "Alice",
        "age": 22,
        "marks": 90,
    }

    print("Keys")

    for key in student.keys():
        print(key)

    print("\nValues")

    for value in student.values():
        print(value)

    print("\nItems")

    for key, value in student.items():
        print(key, value)