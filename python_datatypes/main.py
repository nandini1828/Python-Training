from __future__ import annotations

import argparse
import ast
import json
import logging
from typing import Any, Dict, Optional, Sequence

from .composition.demo import run_composition_demo
from .dictionary_methods.demo import run_dictionary_demo
from .dunder_methods.demo import run_dunder_demo
from .introspection.documentation_extractor import extract_documentation
from .introspection.introspection_engine import introspect_object
from .introspection.method_explorer import explore_methods
from .json_query import resolve_json_path
from .list_methods.demo import run_list_demo
from .logging_config import configure_logging
from .set_methods.demo import run_set_demo
from .tuple_methods.demo import run_tuple_demo

logger = configure_logging()


def parse_literal(expression: str) -> Any:
    try:
        return json.loads(expression)
    except (ValueError, json.JSONDecodeError):
        try:
            return ast.literal_eval(expression)
        except (ValueError, SyntaxError):
            return expression


def format_result(result: Any) -> str:
    try:
        return json.dumps(result, indent=2, default=str)
    except TypeError:
        return str(result)


def run_cli(args: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise-grade Python datatypes toolkit with introspection, JSON query, and demo modules."
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Configure logger verbosity",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    inspect_parser = subparsers.add_parser("introspect", help="Inspect a Python literal or object expression.")
    inspect_parser.add_argument("expression", help="Literal or expression to introspect.")

    query_parser = subparsers.add_parser("query", help="Query a nested JSON or Python structure.")
    query_parser.add_argument("data", help="JSON or Python literal data.")
    query_parser.add_argument("path", help="Query path using dot notation and optional brackets.")

    methods_parser = subparsers.add_parser("methods", help="List callable methods for a type or object.")
    methods_parser.add_argument("expression", help="Literal or expression to inspect.")
    methods_parser.add_argument(
        "--include-dunder",
        action="store_true",
        help="Include dunder methods in the returned list.",
    )

    docs_parser = subparsers.add_parser("docs", help="Extract documentation from a module, class, or function.")
    docs_parser.add_argument("expression", help="Literal or expression to inspect.")

    demo_parser = subparsers.add_parser("demo", help="Execute a built-in demo module.")
    demo_parser.add_argument(
        "module",
        choices=["composition", "dunder", "dictionary", "list", "set", "tuple"],
        help="Demo module to execute.",
    )

    parsed_args = parser.parse_args(args=args)
    logging.getLogger("python_datatypes").setLevel(parsed_args.log_level)
    logger.info("CLI command requested: %s", parsed_args.command)

    if parsed_args.command == "introspect":
        expression_value = parse_literal(parsed_args.expression)
        result = introspect_object(expression_value)
        print(format_result(result))
        return 0

    if parsed_args.command == "query":
        data_value = parse_literal(parsed_args.data)
        result = resolve_json_path(data_value, parsed_args.path)
        print(format_result(result))
        return 0

    if parsed_args.command == "methods":
        expression_value = parse_literal(parsed_args.expression)
        result = explore_methods(expression_value, include_dunder=parsed_args.include_dunder)
        print(format_result(result))
        return 0

    if parsed_args.command == "docs":
        expression_value = parse_literal(parsed_args.expression)
        result = extract_documentation(expression_value)
        print(format_result(result))
        return 0

    if parsed_args.command == "demo":
        demo_map = {
            "composition": run_composition_demo,
            "dunder": run_dunder_demo,
            "dictionary": run_dictionary_demo,
            "list": run_list_demo,
            "set": run_set_demo,
            "tuple": run_tuple_demo,
        }
        demo_map[parsed_args.module]()
        return 0

    parser.print_help()
    return 1


def main() -> None:
    run_cli()


if __name__ == "__main__":
    main()
