from typing import Any


class DunderExamples:

    @staticmethod
    def addition(a: Any, b: Any) -> Any:
        return a.__add__(b)

    @staticmethod
    def equality(a: Any, b: Any) -> bool:
        return a.__eq__(b)

    @staticmethod
    def string_representation(obj: Any) -> str:
        return obj.__str__()