from __future__ import annotations

from argparse_module.argparse_utils import ArgumentParserDemo


def run_argparse_demo() -> None:
    """Show a simple argparse example for beginners."""

    demo = ArgumentParserDemo()
    parsed = demo.parse(["Ada", "--age", "21"])
    print("Name:", parsed.name)
    print("Age:", parsed.age)
