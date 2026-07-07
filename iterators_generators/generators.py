"""
generators.py

Topic:
    - Generators with yield for lazy, memory-safe iteration

Real World Application:
    Streaming product IDs or inventory updates without storing them all in memory
"""


def generate_numbers(limit: int):
    """Yield numbers from 0 up to limit - 1."""
    for number in range(limit):
        yield number


def generate_even_numbers(limit: int):
    """Yield even numbers from 0 up to limit - 1."""
    for number in range(limit):
        if number % 2 == 0:
            yield number


def run() -> None:
    """Run the generator examples."""
    print("\n--- Generators with yield ---")
    print("  Generated numbers:")
    for value in generate_numbers(5):
        print(f"    - {value}")

    print("  Generated even numbers:")
    for value in generate_even_numbers(10):
        print(f"    - {value}")


if __name__ == "__main__":
    run()
