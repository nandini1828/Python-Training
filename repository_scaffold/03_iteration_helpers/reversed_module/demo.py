"""
demo.py

Practical demonstrations of Python's built-in reversed() function.

Run:
    python demo.py
"""


def reverse_list():
    print("\n===== Reverse List =====")

    fruits = ["Apple", "Banana", "Orange", "Mango"]

    for fruit in reversed(fruits):
        print(fruit)


def reverse_string():
    print("\n===== Reverse String =====")

    language = "Python"

    for character in reversed(language):
        print(character)


def reverse_tuple():
    print("\n===== Reverse Tuple =====")

    numbers = (10, 20, 30, 40)

    for number in reversed(numbers):
        print(number)


def reverse_range():
    print("\n===== Reverse Range =====")

    for number in reversed(range(1, 11)):
        print(number)


def reverse_names():
    print("\n===== Reverse Employee List =====")

    employees = [
        "Ganesh",
        "Rahul",
        "Priya",
        "Sneha"
    ]

    for employee in reversed(employees):
        print(employee)


def compare_reverse_methods():
    print("\n===== reversed() vs Slicing =====")

    values = [1, 2, 3, 4, 5]

    print("Using reversed():")
    print(list(reversed(values)))

    print("Using slicing:")
    print(values[::-1])


def reverse_file_lines():
    print("\n===== Reverse File Lines =====")

    lines = [
        "First Line",
        "Second Line",
        "Third Line",
        "Fourth Line"
    ]

    for line in reversed(lines):
        print(line)


def countdown():
    print("\n===== Countdown =====")

    for second in reversed(range(1, 6)):
        print(second)

    print("Launch!")


def reverse_dictionary_keys():
    print("\n===== Reverse Dictionary Keys =====")

    student = {
        "name": "Ganesh",
        "age": 22,
        "course": "Python"
    }

    keys = list(student.keys())

    for key in reversed(keys):
        print(f"{key}: {student[key]}")


def reverse_history():
    print("\n===== Browser History =====")

    history = [
        "google.com",
        "github.com",
        "python.org",
        "openai.com"
    ]

    for page in reversed(history):
        print(page)


def main():
    print("=" * 70)
    print("REVERSED() FUNCTION DEMONSTRATIONS")
    print("=" * 70)

    reverse_list()
    reverse_string()
    reverse_tuple()
    reverse_range()
    reverse_names()
    compare_reverse_methods()
    reverse_file_lines()
    countdown()
    reverse_dictionary_keys()
    reverse_history()

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()