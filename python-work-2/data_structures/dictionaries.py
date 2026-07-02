"""
Dictionary iteration.
"""


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