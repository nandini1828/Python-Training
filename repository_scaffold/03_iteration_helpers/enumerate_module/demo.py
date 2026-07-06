"""
demo.py

Practical demonstrations of Python's built-in enumerate() function.

Run:
    python demo.py
"""


def basic_enumeration():
    print("\n===== Basic Enumeration =====")

    fruits = ["Apple", "Banana", "Orange", "Mango"]

    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")


def custom_start():
    print("\n===== Custom Start Index =====")

    students = ["Ganesh", "Rahul", "Priya", "Sneha"]

    for roll_no, student in enumerate(students, start=101):
        print(f"Roll No {roll_no}: {student}")


def enumerate_string():
    print("\n===== Enumerate String =====")

    language = "Python"

    for position, character in enumerate(language):
        print(f"{position}: {character}")


def enumerate_tuple():
    print("\n===== Enumerate Tuple =====")

    numbers = (10, 20, 30, 40)

    for index, number in enumerate(numbers):
        print(f"{index}: {number}")


def find_student():
    print("\n===== Find Student =====")

    students = ["Anil", "Kiran", "Meena", "Rahul"]

    for index, student in enumerate(students):
        if student == "Meena":
            print(f"Found '{student}' at index {index}")
            break


def create_numbered_menu():
    print("\n===== Numbered Menu =====")

    options = ["Home", "Profile", "Settings", "Logout"]

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")


def track_progress():
    print("\n===== Track Progress =====")

    tasks = ["Download", "Install", "Configure", "Launch"]

    for step, task in enumerate(tasks, start=1):
        print(f"Step {step}: {task}")


def dictionary_from_list():
    print("\n===== Dictionary from List =====")

    cities = ["Hyderabad", "Delhi", "Mumbai"]

    city_map = {}

    for index, city in enumerate(cities):
        city_map[index] = city

    print(city_map)


def enumerate_file_lines():
    print("\n===== Enumerate File Lines =====")

    lines = [
        "First Line",
        "Second Line",
        "Third Line"
    ]

    for line_number, line in enumerate(lines, start=1):
        print(f"{line_number}: {line}")


def compare_manual_counter():
    print("\n===== Manual Counter vs Enumerate =====")

    colors = ["Red", "Green", "Blue"]

    print("Using enumerate():")
    for index, color in enumerate(colors):
        print(index, color)


def main():
    print("=" * 70)
    print("ENUMERATE() FUNCTION DEMONSTRATIONS")
    print("=" * 70)

    basic_enumeration()
    custom_start()
    enumerate_string()
    enumerate_tuple()
    find_student()
    create_numbered_menu()
    track_progress()
    dictionary_from_list()
    enumerate_file_lines()
    compare_manual_counter()

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()