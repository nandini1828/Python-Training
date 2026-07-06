"""
demo.py

Practical demonstrations of Truthy and Falsy values in Python.

Run:
    python demo.py
"""


def bool_function_demo():
    print("\n===== bool() Function =====")

    values = [
        True,
        False,
        1,
        0,
        -10,
        3.14,
        "",
        "Python",
        [],
        [1, 2, 3],
        (),
        (1,),
        {},
        {"name": "Ganesh"},
        set(),
        {1, 2},
        None,
    ]

    for value in values:
        print(f"{repr(value):20} -> {bool(value)}")


def empty_string_demo():
    print("\n===== Empty String =====")

    name = ""

    if name:
        print("Valid Name")
    else:
        print("Name is Empty")


def empty_list_demo():
    print("\n===== Empty List =====")

    numbers = []

    if numbers:
        print("List has elements")
    else:
        print("List is Empty")


def non_empty_list_demo():
    print("\n===== Non-Empty List =====")

    numbers = [10, 20, 30]

    if numbers:
        print("List contains data")


def none_demo():
    print("\n===== None Example =====")

    result = None

    if result is None:
        print("No Result Found")


def zero_demo():
    print("\n===== Zero Example =====")

    number = 0

    if number:
        print("Non-zero")
    else:
        print("Zero evaluates to False")


def dictionary_demo():
    print("\n===== Dictionary Example =====")

    student = {}

    if student:
        print("Student Found")
    else:
        print("Dictionary is Empty")


def set_demo():
    print("\n===== Set Example =====")

    courses = {"Python", "Django"}

    if courses:
        print("Courses Available")


def login_demo():
    print("\n===== Login Validation =====")

    username = "Ganesh"

    if username:
        print("Username Entered")
    else:
        print("Username Missing")


def api_response_demo():
    print("\n===== API Response =====")

    response = {
        "status": 200,
        "data": ["Python", "Django"]
    }

    if response.get("data"):
        print("Records Available")
    else:
        print("No Records")


def file_content_demo():
    print("\n===== File Content =====")

    content = ""

    if not content:
        print("File is Empty")


def shopping_cart_demo():
    print("\n===== Shopping Cart =====")

    cart = ["Laptop", "Mouse"]

    if cart:
        print("Proceed to Checkout")
    else:
        print("Cart is Empty")


def configuration_demo():
    print("\n===== Configuration =====")

    config = None

    if config is None:
        print("Load Default Configuration")


def password_demo():
    print("\n===== Password Validation =====")

    password = "Python123"

    if password:
        print("Password Accepted")
    else:
        print("Password Required")


def database_demo():
    print("\n===== Database Query =====")

    records = []

    if records:
        print("Displaying Records")
    else:
        print("No Records Found")


def main():
    print("=" * 60)
    print("TRUTHY AND FALSY DEMONSTRATIONS")
    print("=" * 60)

    bool_function_demo()
    empty_string_demo()
    empty_list_demo()
    non_empty_list_demo()
    none_demo()
    zero_demo()
    dictionary_demo()
    set_demo()
    login_demo()
    api_response_demo()
    file_content_demo()
    shopping_cart_demo()
    configuration_demo()
    password_demo()
    database_demo()

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()