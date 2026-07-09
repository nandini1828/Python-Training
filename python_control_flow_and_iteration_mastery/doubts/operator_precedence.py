"""
Demonstrates operator precedence and short-circuit evaluation.
"""


class OperatorPrecedenceDemo:

    @staticmethod
    def check_value(name: str, value: bool) -> bool:
        print(f"Evaluating {name}")
        return value

    @staticmethod
    def demonstrate() -> None:

        print("\nExample 1")

        result = (
            OperatorPrecedenceDemo.check_value("A", True)
            or
            OperatorPrecedenceDemo.check_value("B", False)
            and
            OperatorPrecedenceDemo.check_value("C", True)
        )

        print("Result:", result)

        print("\nExample 2")

        result = (
            OperatorPrecedenceDemo.check_value("A", False)
            and
            OperatorPrecedenceDemo.check_value("B", True)
            or
            OperatorPrecedenceDemo.check_value("C", True)
        )

        print("Result:", result)

if __name__ == "__main__":
    OperatorPrecedenceDemo.demonstrate()