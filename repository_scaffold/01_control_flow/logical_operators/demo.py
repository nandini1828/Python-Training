"""
demo.py

Practical demonstrations of Python Logical Operators.

Run:
    python demo.py
"""


def and_demo():
    print("\n===== AND Operator =====")
    age = 20
    citizen = True

    if age >= 18 and citizen:
        print("Eligible to Vote")


def or_demo():
    print("\n===== OR Operator =====")
    is_admin = False
    is_manager = True

    if is_admin or is_manager:
        print("Access Granted")


def not_demo():
    print("\n===== NOT Operator =====")
    logged_in = False

    if not logged_in:
        print("Please Login")


def login_demo():
    print("\n===== Login =====")

    username = "admin"
    password = "python"

    if username == "admin" and password == "python":
        print("Login Successful")
    else:
        print("Invalid Credentials")


def atm_demo():
    print("\n===== ATM =====")

    balance = 10000
    amount = 3000

    if amount <= balance and amount > 0:
        print("Withdrawal Successful")
    else:
        print("Transaction Failed")


def scholarship_demo():
    print("\n===== Scholarship =====")

    marks = 92
    income = 180000

    if marks >= 90 and income < 300000:
        print("Scholarship Approved")


def employee_access():
    print("\n===== Employee Access =====")

    is_employee = True
    has_id = True

    if is_employee and has_id:
        print("Entry Allowed")


def weather_demo():
    print("\n===== Weather =====")

    raining = True
    umbrella = False

    if raining and not umbrella:
        print("Carry an Umbrella")


def discount_demo():
    print("\n===== Discount =====")

    member = True
    amount = 2500

    if member or amount >= 5000:
        print("Discount Applied")


def driving_demo():
    print("\n===== Driving =====")

    age = 22
    license_available = True

    if age >= 18 and license_available:
        print("Can Drive")


def main():
    print("=" * 60)
    print("LOGICAL OPERATORS DEMONSTRATIONS")
    print("=" * 60)

    and_demo()
    or_demo()
    not_demo()
    login_demo()
    atm_demo()
    scholarship_demo()
    employee_access()
    weather_demo()
    discount_demo()
    driving_demo()

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()