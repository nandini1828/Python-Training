"""
demo.py

Practical demonstrations of Python's built-in zip() function.

Run:
    python demo.py
"""


def pair_names_and_marks():
    print("\n===== Pair Names and Marks =====")

    names = ["Ganesh", "Rahul", "Priya", "Sneha"]
    marks = [95, 91, 88, 97]

    for name, mark in zip(names, marks):
        print(f"{name}: {mark}")


def combine_three_lists():
    print("\n===== Combine Three Lists =====")

    names = ["Alice", "Bob", "Charlie"]
    departments = ["IT", "HR", "Finance"]
    salaries = [70000, 65000, 80000]

    for name, department, salary in zip(names, departments, salaries):
        print(f"{name} | {department} | ₹{salary}")


def create_dictionary():
    print("\n===== Create Dictionary =====")

    keys = ["id", "name", "role"]
    values = [101, "Ganesh", "Software Engineer"]

    employee = dict(zip(keys, values))
    print(employee)


def unequal_length_lists():
    print("\n===== Unequal Length Lists =====")

    letters = ["A", "B", "C", "D"]
    numbers = [1, 2]

    for letter, number in zip(letters, numbers):
        print(letter, number)

    print("Iteration stops at the shortest iterable.")


def unzip_data():
    print("\n===== Unzip Data =====")

    records = [
        (1, "Python"),
        (2, "Java"),
        (3, "Go"),
    ]

    ids, languages = zip(*records)

    print("IDs:", ids)
    print("Languages:", languages)


def generate_report():
    print("\n===== Student Report =====")

    students = ["Anil", "Kiran", "Meena"]
    grades = ["A", "B", "A"]

    for student, grade in zip(students, grades):
        print(f"{student} -> Grade {grade}")


def compare_lists():
    print("\n===== Compare Lists =====")

    list_one = [10, 20, 30]
    list_two = [10, 25, 30]

    for first, second in zip(list_one, list_two):
        print(f"{first} == {second}: {first == second}")


def calculate_total_price():
    print("\n===== Calculate Total Price =====")

    products = ["Laptop", "Mouse", "Keyboard"]
    prices = [50000, 800, 1500]

    for product, price in zip(products, prices):
        print(f"{product}: ₹{price}")


def create_employee_records():
    print("\n===== Employee Records =====")

    ids = [101, 102, 103]
    names = ["Ganesh", "Rahul", "Priya"]

    for employee_id, name in zip(ids, names):
        print({"id": employee_id, "name": name})


def pair_coordinates():
    print("\n===== Pair Coordinates =====")

    x_coordinates = [1, 2, 3]
    y_coordinates = [4, 5, 6]

    coordinates = list(zip(x_coordinates, y_coordinates))

    print(coordinates)


def main():
    print("=" * 70)
    print("ZIP() FUNCTION DEMONSTRATIONS")
    print("=" * 70)

    pair_names_and_marks()
    combine_three_lists()
    create_dictionary()
    unequal_length_lists()
    unzip_data()
    generate_report()
    compare_lists()
    calculate_total_price()
    create_employee_records()
    pair_coordinates()

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()