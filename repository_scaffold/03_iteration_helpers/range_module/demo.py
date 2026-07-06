"""
demo.py

Practical demonstrations of Python's built-in range() function.

Run:
    python demo.py
"""


def basic_range():
    print("\n===== Basic Range =====")

    for number in range(5):
        print(number)


def start_stop_range():
    print("\n===== Start and Stop =====")

    for number in range(5, 11):
        print(number)


def step_range():
    print("\n===== Step Value =====")

    for number in range(2, 21, 2):
        print(number)


def reverse_range():
    print("\n===== Reverse Range =====")

    for number in range(10, 0, -1):
        print(number)


def multiplication_table(number):
    print(f"\n===== Multiplication Table of {number} =====")

    for value in range(1, 11):
        print(f"{number} x {value} = {number * value}")


def alphabet_iteration():
    print("\n===== Alphabet Iteration =====")

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for index in range(len(alphabet)):
        print(f"{index} -> {alphabet[index]}")


def list_iteration():
    print("\n===== List Iteration =====")

    fruits = ["Apple", "Banana", "Orange", "Mango"]

    for index in range(len(fruits)):
        print(f"{index}: {fruits[index]}")


def sum_first_n():
    print("\n===== Sum of First N Numbers =====")

    n = 10
    total = 0

    for number in range(1, n + 1):
        total += number

    print("Sum =", total)


def countdown():
    print("\n===== Countdown =====")

    for second in range(5, 0, -1):
        print(second)

    print("Time's Up!")


def nested_range():
    print("\n===== Nested Range =====")

    for row in range(3):
        for column in range(3):
            print(f"({row}, {column})", end=" ")
        print()


def main():
    print("=" * 70)
    print("RANGE() FUNCTION DEMONSTRATIONS")
    print("=" * 70)

    basic_range()
    start_stop_range()
    step_range()
    reverse_range()
    multiplication_table(7)
    alphabet_iteration()
    list_iteration()
    sum_first_n()
    countdown()
    nested_range()

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()