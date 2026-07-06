"""
Practical demonstrations of generator functions.
"""

from .utils import batched, fibonacci, file_lines, filtered_numbers, natural_numbers


def main():
    print("\n===== Generators Demo =====")
    print("Fibonacci:", list(fibonacci(5)))
    print("Natural:", list(natural_numbers(5)))
    print("Filtered:", list(filtered_numbers([1, 5, 2, 8], 4)))
    print("Lines:", list(file_lines(["hello\n", "world"])))
    print("Batched:", list(batched([1, 2, 3, 4, 5], 2)))


if __name__ == "__main__":
    main()
