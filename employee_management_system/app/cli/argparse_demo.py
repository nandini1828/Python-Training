"""Simple CLI example using argparse."""

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Create a small CLI parser with a few commands."""
    parser = argparse.ArgumentParser(description="Employee Management System CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("employees", help="Show employee-related actions")
    subparsers.add_parser("departments", help="Show department-related actions")
    subparsers.add_parser("report", help="Show salary report")
    subparsers.add_parser("analytics", help="Show analytics overview")

    return parser


def main() -> None:
    """Execute the CLI parser."""
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "employees":
        print("Employee command selected")
    elif args.command == "departments":
        print("Departments command selected")
    elif args.command == "report":
        print("Report command selected")
    elif args.command == "analytics":
        print("Analytics command selected")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
