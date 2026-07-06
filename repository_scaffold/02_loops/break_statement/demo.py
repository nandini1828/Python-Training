"""
demo.py

Practical demonstrations of Python's break statement.

Run:
    python demo.py
"""


def stop_at_number():
    print("\n===== Stop at Number =====")

    for number in range(1, 11):
        if number == 6:
            break

        print(number)


def search_element():
    print("\n===== Search Element =====")

    numbers = [10, 20, 30, 40, 50]

    target = 30

    for number in numbers:
        if number == target:
            print(f"{target} Found")
            break


def first_even():
    print("\n===== First Even Number =====")

    numbers = [1, 3, 5, 8, 9]

    for number in numbers:
        if number % 2 == 0:
            print(number)
            break


def login_attempt():
    print("\n===== Login Attempts =====")

    attempts = 3

    while attempts > 0:
        print(f"Attempt {4 - attempts}")

        success = attempts == 2

        if success:
            print("Login Successful")
            break

        attempts -= 1


def stop_file_processing():
    print("\n===== File Processing =====")

    lines = [
        "Python",
        "Java",
        "ERROR",
        "Go",
        "Rust"
    ]

    for line in lines:
        if line == "ERROR":
            print("Error Found")
            break

        print(line)


def stop_on_negative():
    print("\n===== Stop on Negative =====")

    values = [5, 8, 12, -1, 20]

    for value in values:
        if value < 0:
            break

        print(value)


def find_prime():
    print("\n===== Find First Prime =====")

    numbers = [8, 10, 15, 17, 20]

    for number in numbers:
        is_prime = True

        if number < 2:
            continue

        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            print(number)
            break


def menu_exit():
    print("\n===== Menu Exit =====")

    options = ["Home", "Profile", "Exit", "Settings"]

    for option in options:
        if option == "Exit":
            print("Closing Application...")
            break

        print(option)


def process_orders():
    print("\n===== Order Processing =====")

    orders = ["Order-1", "Order-2", "Cancelled", "Order-3"]

    for order in orders:
        if order == "Cancelled":
            print("Stopping Processing")
            break

        print(order)


def infinite_loop_break():
    print("\n===== Infinite Loop with Break =====")

    counter = 1

    while True:
        print(counter)

        if counter == 5:
            break

        counter += 1


def main():
    print("=" * 70)
    print("BREAK STATEMENT DEMONSTRATIONS")
    print("=" * 70)

    stop_at_number()
    search_element()
    first_even()
    login_attempt()
    stop_file_processing()
    stop_on_negative()
    find_prime()
    menu_exit()
    process_orders()
    infinite_loop_break()

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()