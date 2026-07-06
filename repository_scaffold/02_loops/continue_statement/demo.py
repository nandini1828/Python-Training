"""
demo.py

Demonstrations of Python continue statement.

Run:
    python demo.py
"""


def skip_even_numbers():
    print("\n===== Skip Even Numbers =====")

    for i in range(1, 11):
        if i % 2 == 0:
            continue
        print(i)


def skip_negative_values():
    print("\n===== Skip Negative Values =====")

    values = [10, -5, 20, -1, 30]

    for val in values:
        if val < 0:
            continue
        print(val)


def skip_empty_strings():
    print("\n===== Skip Empty Strings =====")

    names = ["Ganesh", "", "Rahul", "", "Sita"]

    for name in names:
        if name == "":
            continue
        print(name)


def skip_multiples_of_three():
    print("\n===== Skip Multiples of 3 =====")

    for i in range(1, 16):
        if i % 3 == 0:
            continue
        print(i)


def skip_invalid_emails():
    print("\n===== Skip Invalid Emails =====")

    emails = ["a@gmail.com", "invalid", "b@yahoo.com", "test"]

    for email in emails:
        if "@" not in email:
            continue
        print(email)


def skip_zero_division():
    print("\n===== Skip Zero Division =====")

    numbers = [10, 5, 0, 2]

    for num in numbers:
        if num == 0:
            continue
        print(10 / num)


def process_students():
    print("\n===== Process Students =====")

    students = [
        {"name": "A", "marks": 90},
        {"name": "B", "marks": -1},  # invalid
        {"name": "C", "marks": 75},
    ]

    for student in students:
        if student["marks"] < 0:
            continue
        print(student["name"], student["marks"])


def main():
    print("=" * 70)
    print("CONTINUE STATEMENT DEMONSTRATIONS")
    print("=" * 70)

    skip_even_numbers()
    skip_negative_values()
    skip_empty_strings()
    skip_multiples_of_three()
    skip_invalid_emails()
    skip_zero_division()
    process_students()

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()