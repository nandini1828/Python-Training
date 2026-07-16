import argparse

from app.models.address import Address
from app.models.student import Student


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a student from the command line.")
    parser.add_argument("--name", required=True)
    parser.add_argument("--age", required=True, type=int)
    parser.add_argument("--city", required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    student = Student(name=args.name, age=args.age, address=Address(city=args.city))
    print(student.introduce())


if __name__ == "__main__":
    main()
