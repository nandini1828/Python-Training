from .utils import *

def run_demo():
    print("Range Demo\n")

    print("Default Range:")
    print(generate_numbers(5))

    print("\nCustom Range:")
    print(generate_custom_range(1, 10, 2))

    print("\nEven Numbers:")
    print(even_numbers(10))

    print("\nOdd Numbers:")
    print(odd_numbers(10))

    print("\nSum:")
    print(sum_of_range(10))


if __name__ == "__main__":
    run_demo()