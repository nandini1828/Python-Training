"""Example programs for Data Structures section.
"""

def list_demo():
    numbers = [10, 20, 30]
    numbers.append(40)
    numbers.remove(20)
    print("list_demo ->", numbers)


def tuple_demo():
    colors = ("Red", "Green", "Blue")
    print("tuple_demo -> first color:", colors[0])
    print("tuple_demo -> length:", len(colors))


def dictionary_demo():
    employee = {
        "name": "Vamshi",
        "salary": 50000,
    }
    employee["department"] = "IT"
    print("dictionary_demo ->", employee)


def set_demo():
    numbers = {1, 2, 3}
    numbers.add(4)
    numbers.add(2)  # duplicate ignored
    print("set_demo ->", numbers)


if __name__ == "__main__":
    print("Running data structures examples...\n")
    list_demo()
    print()
    tuple_demo()
    print()
    dictionary_demo()
    print()
    set_demo()
