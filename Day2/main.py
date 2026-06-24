from __future__ import annotations

import argparse
import logging
from typing import Sequence

from composition.demo import run_composition_demo
from dictionary_methods.demo import run_dictionary_demo
from dunder_methods.demo import run_dunder_demo
from introspection.demo import run_introspection_demo
from list_methods.demo import run_list_demo
from set_methods.demo import run_set_demo
from tuple_methods.demo import run_tuple_demo

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("python_learning_framework")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Professional Python learning framework")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("introspection", help="Run introspection examples")
    subparsers.add_parser("dictionary", help="Run dictionary examples")
    subparsers.add_parser("list", help="Run list examples")
    subparsers.add_parser("set", help="Run set examples")
    subparsers.add_parser("tuple", help="Run tuple examples")
    subparsers.add_parser("dunder", help="Run dunder method examples")
    subparsers.add_parser("composition", help="Run composition examples")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    logger.info("CLI command received: %s", args.command)

    if args.command == "introspection":
        run_introspection_demo()
    elif args.command == "dictionary":
        run_dictionary_demo()
    elif args.command == "list":
        run_list_demo()
    elif args.command == "set":
        run_set_demo()
    elif args.command == "tuple":
        run_tuple_demo()
    elif args.command == "dunder":
        run_dunder_demo()
    elif args.command == "composition":
        run_composition_demo()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
