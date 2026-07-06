"""
demo.py

Practical demonstrations of Python while loops.

Run:
    python demo.py
"""


def basic_counting():
    print("\n===== Basic Counting =====")

    count = 1

    while count <= 5:
        print(count)
        count += 1


def reverse_counting():
    print("\n===== Reverse Counting =====")

    count = 5

    while count >= 1:
        print(count)
        count -= 1


def sum_numbers():
    print("\n===== Sum of Numbers =====")

    numbers = [10, 20, 30, 40]

    index = 0
    total = 0

    while index < len(numbers):
        total += numbers[index]
        index += 1

    print("Total =", total)


def factorial():
    print("\n===== Factorial =====")

    number = 5
    result = 1

    while number > 1:
        result *= number
        number -= 1

    print("Factorial =", result)


def multiplication_table():
    print("\n===== Multiplication Table =====")

    number = 7
    value = 1

    while value <= 10:
        print(f"{number} x {value} = {number * value}")
        value += 1


def password_attempts():
    print("\n===== Password Attempts =====")

    attempts = 3

    while attempts > 0:
        print(f"Attempts Remaining : {attempts}")
        attempts -= 1

    print("Account Locked")


def process_queue():
    print("\n===== Queue Processing =====")

    queue = ["Task-1", "Task-2", "Task-3"]

    while queue:
        print("Processing", queue.pop(0))


def retry_connection():
    print("\n===== Retry Connection =====")

    retries = 0
    max_retries = 3

    while retries < max_retries:
        print(f"Attempt {retries + 1}")
        retries += 1

    print("Maximum retries reached.")


def countdown():
    print("\n===== Countdown =====")

    seconds = 5

    while seconds > 0:
        print(seconds)
        seconds -= 1

    print("Time's Up!")


def find_first_even():
    print("\n===== Find First Even =====")

    numbers = [1, 3, 5, 8, 9]

    index = 0

    while index < len(numbers):
        if numbers[index] % 2 == 0:
            print("First Even =", numbers[index])
            break

        index += 1


def main():
    print("=" * 70)
    print("WHILE LOOP DEMONSTRATIONS")
    print("=" * 70)

    basic_counting()
    reverse_counting()
    sum_numbers()
    factorial()
    multiplication_table()
    password_attempts()
    process_queue()
    retry_connection()
    countdown()
    find_first_even()

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()