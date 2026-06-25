"""
==================================================
Module: Argparse Utilities
Topic: Command Line Arguments

Description:
A beginner-friendly class for parsing simple
command-line arguments.
==================================================
"""

from __future__ import annotations

import argparse


class ArgumentParserDemo:
    """A simple wrapper around argparse for beginner examples."""

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="Simple argument parser demo")
        self.parser.add_argument("name", help="Your name")
        self.parser.add_argument("--age", type=int, default=0, help="Your age")

    def parse(self, args: list[str] | None = None) -> argparse.Namespace:
        """Parse command-line arguments."""
        return self.parser.parse_args(args)
