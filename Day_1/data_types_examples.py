"""Example programs for Data Types section.
"""

def type_conversion_demo():
    age = "25"
    age = int(age)
    salary = 50000
    salary = float(salary)
    print("type_conversion_demo -> age:", age, type(age))
    print("type_conversion_demo -> salary:", salary, type(salary))


def mutable_immutable_demo():
    number = 10
    number += 5  # integers are immutable; this creates a new int object
    fruits = ["Apple", "Banana"]
    fruits.append("Mango")  # lists are mutable
    print("mutable_immutable_demo -> number:", number)
    print("mutable_immutable_demo -> fruits:", fruits)


def data_types_demo():
    name = "Vamshi"
    age = 25
    salary = 45000.50
    is_employee = True
    print("data_types_demo -> name type:", type(name))
    print("data_types_demo -> age type:", type(age))
    print("data_types_demo -> salary type:", type(salary))
    print("data_types_demo -> is_employee type:", type(is_employee))


if __name__ == "__main__":
    print("Running data types examples...\n")
    type_conversion_demo()
    print()
    mutable_immutable_demo()
    print()
    data_types_demo()
