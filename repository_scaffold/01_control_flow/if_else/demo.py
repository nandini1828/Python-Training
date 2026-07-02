"""
demo.py

Practical demonstrations of Python's if-elif-else statements.

Run:
    python demo.py
"""


def basic_if():
    print("\n===== Basic if =====")

    age = 20

    if age >= 18:
        print("Adult")


def if_else():
    print("\n===== if-else =====")

    age = 15

    if age >= 18:
        print("Adult")
    else:
        print("Minor")


def if_elif_else():
    print("\n===== if-elif-else =====")

    marks = 82

    if marks >= 90:
        print("Grade A")

    elif marks >= 75:
        print("Grade B")

    elif marks >= 60:
        print("Grade C")

    else:
        print("Fail")


def nested_if():
    print("\n===== Nested if =====")

    age = 24
    citizen = True

    if age >= 18:
        if citizen:
            print("Eligible to Vote")
        else:
            print("Not a Citizen")
    else:
        print("Minor")


def positive_negative():
    print("\n===== Positive or Negative =====")

    number = -5

    if number > 0:
        print("Positive Number")

    elif number < 0:
        print("Negative Number")

    else:
        print("Zero")


def even_odd():
    print("\n===== Even or Odd =====")

    number = 24

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


def largest_number():
    print("\n===== Largest Number =====")

    a = 25
    b = 18

    if a > b:
        print(f"{a} is larger")
    else:
        print(f"{b} is larger")


def leap_year():
    print("\n===== Leap Year =====")

    year = 2024

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")


def login_system():
    print("\n===== Login System =====")

    username = "admin"
    password = "python"

    if username == "admin" and password == "python":
        print("Login Successful")
    else:
        print("Invalid Credentials")


def atm_withdrawal():
    print("\n===== ATM Withdrawal =====")

    balance = 10000
    withdrawal = 2500

    if withdrawal <= balance:
        balance -= withdrawal
        print("Transaction Successful")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")


def shopping_discount():
    print("\n===== Shopping Discount =====")

    amount = 1500

    if amount >= 2000:
        discount = 20

    elif amount >= 1000:
        discount = 10

    else:
        discount = 5

    print(f"Discount: {discount}%")


def employee_bonus():
    print("\n===== Employee Bonus =====")

    rating = 5

    if rating == 5:
        print("Bonus: ₹50,000")

    elif rating == 4:
        print("Bonus: ₹30,000")

    else:
        print("Bonus: ₹10,000")


def weather_system():
    print("\n===== Weather Advisory =====")

    weather = "Rainy"

    if weather == "Sunny":
        print("Go Outside")

    elif weather == "Rainy":
        print("Carry an Umbrella")

    else:
        print("Stay Safe")


def traffic_signal():
    print("\n===== Traffic Signal =====")

    signal = "Green"

    if signal == "Red":
        print("STOP")

    elif signal == "Yellow":
        print("READY")

    elif signal == "Green":
        print("GO")

    else:
        print("Invalid Signal")


def student_result():
    print("\n===== Student Result =====")

    marks = 67

    if marks >= 90:
        grade = "A"

    elif marks >= 75:
        grade = "B"

    elif marks >= 60:
        grade = "C"

    elif marks >= 40:
        grade = "D"

    else:
        grade = "Fail"

    print("Grade:", grade)


def main():
    print("=" * 60)
    print("PYTHON IF-ELIF-ELSE DEMONSTRATIONS")
    print("=" * 60)

    basic_if()
    if_else()
    if_elif_else()
    nested_if()
    positive_negative()
    even_odd()
    largest_number()
    leap_year()
    login_system()
    atm_withdrawal()
    shopping_discount()
    employee_bonus()
    weather_system()
    traffic_signal()
    student_result()

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()