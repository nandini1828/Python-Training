"""
demo.py

Demonstration of pass statement usage.

Run:
    python demo.py
"""

from .utils import process_positive_numbers, find_first_positive, placeholder_function


def demo_process_positive_numbers():
    print("\n--- Process Positive Numbers ---")
    data = [3, -1, 5, -7, 9]
    print(process_positive_numbers(data))  # [3, 5, 9]


def demo_find_first_positive():
    print("\n--- Find First Positive ---")
    print(find_first_positive([-5, -2, 0, 4, 6]))  # 4
    print(find_first_positive([-5, -2, 0]))        # None


def demo_placeholder():
    print("\n--- Placeholder Function ---")
    result = placeholder_function()
    print(result)  # None


def main():
    print("=" * 60)
    print("PASS STATEMENT DEMO")
    print("=" * 60)

    demo_process_positive_numbers()
    demo_find_first_positive()
    demo_placeholder()

    print("\nAll demos executed successfully.")


if __name__ == "__main__":
    main()