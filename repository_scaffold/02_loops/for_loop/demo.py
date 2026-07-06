"""
demo.py

Practical demonstrations of Python for loops.

Run:
    python demo.py
"""


def iterate_list():
    print("\n===== Iterate over List =====")

    fruits = ["Apple", "Banana", "Orange", "Mango"]

    for fruit in fruits:
        print(fruit)


def iterate_tuple():
    print("\n===== Iterate over Tuple =====")

    numbers = (10, 20, 30, 40)

    for number in numbers:
        print(number)


def iterate_string():
    print("\n===== Iterate over String =====")

    language = "Python"

    for character in language:
        print(character)


def iterate_range():
    print("\n===== Iterate using range() =====")

    for number in range(1, 6):
        print(number)


def iterate_dictionary():
    print("\n===== Iterate over Dictionary =====")

    employee = {
        "id": 101,
        "name": "Ganesh",
        "role": "Software Engineer"
    }

    for key, value in employee.items():
        print(f"{key} : {value}")


def iterate_set():
    print("\n===== Iterate over Set =====")

    technologies = {"Python", "Django", "FastAPI", "React"}

    for technology in technologies:
        print(technology)


def nested_loop():
    print("\n===== Nested Loop =====")

    for row in range(3):
        for column in range(3):
            print(f"({row}, {column})", end=" ")
        print()


def multiplication_table(number):
    print(f"\n===== Multiplication Table of {number} =====")

    for value in range(1, 11):
        print(f"{number} x {value} = {number * value}")


def sum_of_numbers():
    print("\n===== Sum of Numbers =====")

    numbers = [5, 10, 15, 20]

    total = 0

    for number in numbers:
        total += number

    print("Total =", total)


def iterate_file_lines():
    print("\n===== Simulated File Processing =====")

    lines = [
        "Python",
        "Java",
        "C++",
        "Go"
    ]

    for line in lines:
        print(line)


def main():
    print("=" * 70)
    print("FOR LOOP DEMONSTRATIONS")
    print("=" * 70)

    iterate_list()
    iterate_tuple()
    iterate_string()
    iterate_range()
    iterate_dictionary()
    iterate_set()
    nested_loop()
    multiplication_table(7)
    sum_of_numbers()
    iterate_file_lines()

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()