"""
Demo application for python_datatypes_mastery.

This script runs concise demonstrations of the modules in the package.
"""
from __future__ import annotations

from __future__ import annotations

import argparse
import subprocess
from typing import Any

from python_datatypes_mastery.primitives.introspection import inspect_object
from python_datatypes_mastery.primitives.casting import safe_cast
from python_datatypes_mastery.primitives.dunder_examples import Employee, demo_dunders
from python_datatypes_mastery.collections_pkg.list_utils import demo_list_methods
from python_datatypes_mastery.collections_pkg.dict_utils import demo_dict_methods
from python_datatypes_mastery.collections_pkg.set_utils import demo_set_methods
from python_datatypes_mastery.classes.student import Student
from python_datatypes_mastery.classes.computer import CPU, Computer
from python_datatypes_mastery.classes.object_deconstructor import deconstruct_object
from python_datatypes_mastery.inspectors.method_inspector import get_methods_and_docs
from python_datatypes_mastery.exercises.queue import SimpleQueue
from python_datatypes_mastery.exercises.json_query import query_json


def demo_introspection() -> None:
    """Demonstrate introspection utilities."""
    print("--- Introspection ---")
    sample = [1, "two", {"three": 3}]
    print(inspect_object(sample))


def demo_casting() -> None:
    """Demonstrate safe casting examples."""
    print("\n--- Casting ---")
    print(safe_cast("123", int, default=0))
    print(safe_cast("bad", int, default=-1))


def demo_dunder_methods() -> None:
    """Demonstrate custom dunder behaviors."""
    print("\n--- Dunder Methods ---")
    emp_a = Employee("Alice", salary=70000)
    emp_b = Employee("Bob", salary=50000)
    print(emp_a + emp_b)
    print(repr(emp_a))
    demo_dunders()


def demo_collections() -> None:
    """Demonstrate list, dict and set utilities."""
    print("\n--- Lists / Dicts / Sets ---")
    print(demo_list_methods([1, 2, 3], [4, 5]))
    print(demo_dict_methods({"a": 1}, {"b": 2}))
    print(demo_set_methods({1, 2}, {2, 3}))


def demo_classes_and_composition() -> None:
    """Demonstrate classes, composition and object internals."""
    print("\n--- Classes & Composition ---")
    student = Student("Charlie", [88, 92, 75])
    print(student.__dict__)
    print("Average (unbound):", Student.average_grade(student))

    cpu = CPU(cores=4, frequency_ghz=3.2)
    computer = Computer(brand="ExampleBrand", cpu=cpu)
    print(computer.__dict__)


def demo_deconstruction() -> None:
    """Demonstrate recursive object deconstruction to primitives."""
    print("\n--- Object Deconstruction ---")
    cpu = CPU(cores=4, frequency_ghz=3.2)
    computer = Computer(brand="ExampleBrand", cpu=cpu)
    print(deconstruct_object(computer))


def demo_inspectors() -> None:
    """Demonstrate method and documentation inspectors."""
    print("\n--- Inspectors ---")
    print(get_methods_and_docs([]))


def demo_queue_and_json() -> None:
    """Demonstrate SimpleQueue and JSON querying."""
    print("\n--- Queue & JSON Query ---")
    q = SimpleQueue()
    q.enqueue(10)
    q.enqueue(20)
    print("Queue size:", q.size())
    print("Dequeue:", q.dequeue())

    data = {"user": {"profile": {"name": "Dana"}}}
    print(query_json(data, "user.profile.name"))


def run_demo() -> None:
    """Run all demo sections (backwards-compatible)."""
    demo_introspection()
    demo_casting()
    demo_dunder_methods()
    demo_collections()
    demo_classes_and_composition()
    demo_deconstruction()
    demo_inspectors()
    demo_queue_and_json()


def run_pytest() -> int:
    """Run pytest programmatically and return exit code.

    Returns:
        The exit code from the pytest subprocess.
    """
    result = subprocess.run(["pytest", "-q"], cwd="..")
    return result.returncode


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="python_datatypes_mastery demo runner")
    parser.add_argument("--all", action="store_true", help="Run all demo sections")
    parser.add_argument("--introspection", action="store_true", help="Run introspection demo")
    parser.add_argument("--casting", action="store_true", help="Run casting demo")
    parser.add_argument("--dunder", action="store_true", help="Run dunder methods demo")
    parser.add_argument("--collections", action="store_true", help="Run collections demo")
    parser.add_argument("--classes", action="store_true", help="Run classes/composition demo")
    parser.add_argument("--deconstruct", action="store_true", help="Run object deconstruction demo")
    parser.add_argument("--inspectors", action="store_true", help="Run inspectors demo")
    parser.add_argument("--queue", action="store_true", help="Run queue/json demo")
    parser.add_argument("--run-tests", action="store_true", help="Run pytest for the project")
    return parser


def main(argv: Any | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.run_tests:
        return run_pytest()

    did_any = False
    if args.all or not any(vars(args).values()):
        run_demo()
        did_any = True

    if args.introspection:
        demo_introspection(); did_any = True
    if args.casting:
        demo_casting(); did_any = True
    if args.dunder:
        demo_dunder_methods(); did_any = True
    if args.collections:
        demo_collections(); did_any = True
    if args.classes:
        demo_classes_and_composition(); did_any = True
    if args.deconstruct:
        demo_deconstruction(); did_any = True
    if args.inspectors:
        demo_inspectors(); did_any = True
    if args.queue:
        demo_queue_and_json(); did_any = True

    return 0 if did_any else 1


if __name__ == "__main__":
    raise SystemExit(main())
