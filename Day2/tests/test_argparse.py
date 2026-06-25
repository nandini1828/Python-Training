from __future__ import annotations

from argparse_module.argparse_utils import ArgumentParserDemo


def test_argument_parser_demo_parses_arguments() -> None:
    demo = ArgumentParserDemo()
    parsed = demo.parse(["Ada", "--age", "21"])
    assert parsed.name == "Ada"
    assert parsed.age == 21
