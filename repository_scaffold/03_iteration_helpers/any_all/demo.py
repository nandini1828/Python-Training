"""
demo.py

Practical demonstrations of Python's built-in any() and all() functions.

Run:
    python demo.py
"""


def any_with_numbers():
    print("\n===== any() with Numbers =====")

    numbers = [0, 0, 5, 0]

    print(any(numbers))


def all_even_numbers():
    print("\n===== all() with Even Numbers =====")

    numbers = [2, 4, 6, 8]

    print(all(number % 2 == 0 for number in numbers))


def any_positive_number():
    print("\n===== Any Positive Number =====")

    values = [-5, -2, 0, 8]

    print(any(value > 0 for value in values))


def all_positive_numbers():
    print("\n===== All Positive Numbers =====")

    values = [5, 10, 15, 20]

    print(all(value > 0 for value in values))


def validate_passwords():
    print("\n===== Password Validation =====")

    passwords = [
        "Python@123",
        "Secure#456",
        "Admin789!"
    ]

    print(all(len(password) >= 8 for password in passwords))


def check_text_files():
    print("\n===== Text File Check =====")

    files = [
        "report.pdf",
        "notes.txt",
        "image.png"
    ]

    print(any(file.endswith(".txt") for file in files))


def verify_student_marks():
    print("\n===== Student Marks =====")

    marks = [85, 76, 92, 88]

    print(all(mark >= 35 for mark in marks))


def check_empty_strings():
    print("\n===== Empty String Check =====")

    values = ["Python", "", "Programming"]

    print(any(not value for value in values))


def user_permissions():
    print("\n===== User Permissions =====")

    permissions = ["read", "write", "execute"]

    print(all(permission in permissions for permission in ["read", "write"]))


def api_response_validation():
    print("\n===== API Response Validation =====")

    response = {
        "id": 101,
        "name": "Ganesh",
        "email": "ganesh@example.com"
    }

    required_fields = ["id", "name", "email"]

    print(all(field in response for field in required_fields))


def main():
    print("=" * 70)
    print("ANY() AND ALL() FUNCTION DEMONSTRATIONS")
    print("=" * 70)

    any_with_numbers()
    all_even_numbers()
    any_positive_number()
    all_positive_numbers()
    validate_passwords()
    check_text_files()
    verify_student_marks()
    check_empty_strings()
    user_permissions()
    api_response_validation()

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()