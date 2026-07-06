"""Command-line interface for the python_datatypes learning package.

Provides subcommands for introspection, JSON querying and demo utilities.
"""

from __future__ import annotations

import argparse
import json
import logging
from typing import Any

from introspection import inspect_object, get_methods
from utils import query_json
from composition.composition_example import Computer
from dunder_methods.dunder_examples import BankAccount
from list_methods.list_utils import unique, chunk
from set_methods.set_utils import union, intersection, is_subset
from tuple_methods.tuple_utils import to_list, count_value
from list_methods.demo import main as list_demo_main
from tuple_methods.demo import main as tuple_demo_main
from set_methods.demo import main as set_demo_main
from dictionary_methods.demo import main as dict_demo_main
from dunder_methods.demo import main as dunder_demo_main
from composition.demo import main as composition_demo_main
from introspection.demo import main as introspection_demo_main

logger = logging.getLogger("python_datatypes")


def setup_logging(level: int = logging.INFO) -> None:
    """Configure root logger."""

    handler = logging.StreamHandler()
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    handler.setFormatter(fmt)
    root = logging.getLogger()
    root.setLevel(level)
    if not root.handlers:
        root.addHandler(handler)


def cli_introspect(args: argparse.Namespace) -> None:
    """Handle `introspect` subcommand."""

    target = args.object
    logger.info("Running introspection for: %s", target)

    sample: Any
    if target == "list":
        sample = [1, 2, 3]
    elif target == "dict":
        sample = {"a": 1}
    elif target == "tuple":
        sample = (1, 2)
    elif target == "set":
        sample = {1, 2}
    elif target == "bank":
        sample = BankAccount("Alice", 1000)
    elif target == "computer":
        sample = Computer()
    else:
        # fallback: try to evaluate builtin name
        try:
            sample = eval(target)
        except Exception:
            sample = target

    info = inspect_object(sample)
    print(json.dumps(info, indent=2, default=str))


def cli_json_query(args: argparse.Namespace) -> None:
    logger.info("Running json-query on file %s path %s", args.file, args.path)
    with open(args.file, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    result = query_json(data, args.path)
    print(json.dumps(result, indent=2, default=str))


def main(argv: list[str] | None = None) -> None:
    setup_logging()

    parser = argparse.ArgumentParser(prog="python_datatypes")
    sub = parser.add_subparsers(dest="command")

    p_ins = sub.add_parser("introspect", help="Inspect a Python object")
    p_ins.add_argument("--object", required=True, help="Object to inspect (list|dict|tuple|set|bank|computer|<expr>)")
    p_ins.set_defaults(func=cli_introspect)

    p_json = sub.add_parser("json-query", help="Query a JSON file for a dotted path")
    p_json.add_argument("--file", required=True, help="Path to JSON file")
    p_json.add_argument("--path", required=True, help="Dotted path to query")
    p_json.set_defaults(func=cli_json_query)

    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        # Interactive fallback when no subcommand provided
        interactive_menu()
        return
    args.func(args)


def interactive_menu() -> None:
    """Simple interactive menu when CLI is invoked without subcommands."""

    while True:
        print("\nPython Datatypes — Interactive Menu:\n")
        print("1. Introspect an object")
        print("2. JSON query (file + dotted path)")
        print("3. Run demo modules")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        if choice == "1":
            obj = input("Enter object (list|dict|tuple|set|bank|computer|literal): ")
            ns = argparse.Namespace(object=obj)
            cli_introspect(ns)
            continue
        if choice == "2":
            file = input("JSON file path [samples/sample.json]: ") or "samples/sample.json"
            path = input("Dotted path (eg. user.address.city): ")
            ns = argparse.Namespace(file=file, path=path)
            try:
                cli_json_query(ns)
            except FileNotFoundError:
                print("File not found:", file)
            continue
        if choice == "3":
            print("\nDemos:\n1. Introspection\n2. Composition\n3. Dunder\n4. List\n5. Tuple\n6. Set\n7. Dictionary\n")
            sel = input("Choose demo: ").strip()
            if sel == "1":
                introspection_demo_main()
            elif sel == "2":
                composition_demo_main()
            elif sel == "3":
                dunder_demo_main()
            elif sel == "4":
                list_demo_main()
            elif sel == "5":
                tuple_demo_main()
            elif sel == "6":
                set_demo_main()
            elif sel == "7":
                dict_demo_main()
            else:
                print("Invalid demo selection")
            continue
        print("Invalid choice, try again.")


if __name__ == "__main__":
    main()