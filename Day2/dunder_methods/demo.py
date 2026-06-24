from __future__ import annotations

from dunder_methods.dunder_utils import DunderDemo


def run_dunder_demo() -> None:
    """Show simple dunder methods with a beginner-friendly example."""

    first = DunderDemo("Ada", 37)
    second = DunderDemo("Ada", 37)
    third = DunderDemo("Grace", 32)

    print("Representation:", repr(first))
    print("String form:", str(first))
    print("Equal:", first == second)
    print("Compare age:", first < third)
