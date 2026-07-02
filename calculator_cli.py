"""
argparse.py

Demonstrates how to use Python's argparse module for
handling command-line arguments.

Run Examples:

1. Addition
python argparse.py add 10 20

2. Subtraction
python argparse.py subtract 20 5

3. Multiplication
python argparse.py multiply 5 6

4. Division
python argparse.py divide 20 4

5. Verbose Output
python argparse.py add 10 20 --verbose

6. Greeting
python argparse.py add 10 20 --name Karthik
"""

import argparse


def main():
    # Create parser
    parser = argparse.ArgumentParser(
        description="Simple Calculator using argparse"
    )

    # Positional arguments
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="Operation to perform",
    )

    parser.add_argument(
        "num1",
        type=float,
        help="First number",
    )

    parser.add_argument(
        "num2",
        type=float,
        help="Second number",
    )

    # Optional argument
    parser.add_argument(
        "--name",
        type=str,
        default="User",
        help="Your name",
    )

    # Flag argument
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Display detailed output",
    )

    # Parse arguments
    args = parser.parse_args()

    # Perform operation
    if args.operation == "add":
        result = args.num1 + args.num2

    elif args.operation == "subtract":
        result = args.num1 - args.num2

    elif args.operation == "multiply":
        result = args.num1 * args.num2

    else:
        if args.num2 == 0:
            print("Division by zero is not allowed.")
            return
        result = args.num1 / args.num2

    # Output
    if args.verbose:
        print(f"Hello, {args.name}!")
        print(f"Operation : {args.operation}")
        print(f"First Number : {args.num1}")
        print(f"Second Number : {args.num2}")
        print(f"Result : {result}")
    else:
        print(result)


if __name__ == "__main__":
    main()