"""
demo.py

Practical demonstrations of Python Short-Circuit Evaluation.

Run:
    python demo.py
"""


def and_short_circuit():
    print("\n===== AND Short-Circuit =====")

    age = 16

    if age >= 18 and age < 60:
        print("Eligible")
    else:
        print("Not Eligible")


def or_short_circuit():
    print("\n===== OR Short-Circuit =====")

    username = ""

    display_name = username or "Guest"

    print(f"Welcome {display_name}")


def safe_division():
    print("\n===== Safe Division =====")

    numerator = 100
    denominator = 0

    result = denominator != 0 and numerator / denominator

    print("Result:", result)


def login_validation():
    print("\n===== Login Validation =====")

    username = "Ganesh"
    password = "python123"

    authenticated = username and password

    if authenticated:
        print("Login Successful")
    else:
        print("Invalid Credentials")


def api_response():
    print("\n===== API Response =====")

    response = {
        "status": 200,
        "data": {
            "name": "Ganesh"
        }
    }

    name = (
        response
        and response.get("data")
        and response["data"].get("name")
    )

    print(name)


def configuration_loading():
    print("\n===== Configuration =====")

    user_config = None

    config = user_config or "Default Configuration"

    print(config)


def shopping_cart():
    print("\n===== Shopping Cart =====")

    cart = ["Laptop", "Mouse"]

    if cart and len(cart) > 0:
        print("Checkout Available")
    else:
        print("Cart is Empty")


def file_processing():
    print("\n===== File Processing =====")

    file_content = ""

    content = file_content or "Using Backup File"

    print(content)


def employee_access():
    print("\n===== Employee Access =====")

    is_employee = True
    has_id = False

    if is_employee and has_id:
        print("Access Granted")
    else:
        print("Access Denied")


def expensive_operation():
    print("\n===== Expensive Operation =====")

    cache = {
        "python": "Programming Language"
    }

    value = cache.get("python") or "Fetching from Database..."

    print(value)


def main():
    print("=" * 70)
    print("SHORT-CIRCUIT EVALUATION DEMONSTRATIONS")
    print("=" * 70)

    and_short_circuit()
    or_short_circuit()
    safe_division()
    login_validation()
    api_response()
    configuration_loading()
    shopping_cart()
    file_processing()
    employee_access()
    expensive_operation()

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()