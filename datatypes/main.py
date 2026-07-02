"""
Main entry point for the Python Training application with a simple CLI.

This script demonstrates all training modules and provides a lightweight
command-line interface to run the demo or the test-suite.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from typing import Optional

from datatypes.primitive_datatypes import PrimitiveManager
from datatypes.type_casting import SafeCast, NumericCasting
from datatypes.introspection import ObjectInspector
from datatypes.classes import ClassManager
from datatypes.dunder_methods import CustomNumber, CustomString
from datatypes.data_structure_methods.lists import ListManager
from datatypes.data_structure_methods.sets import SetManager
from datatypes.data_structure_methods.dictionaries import DictionaryManager


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the training CLI."""
    parser = argparse.ArgumentParser(description="Python Training CLI")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--demo", action="store_true", help="Run the interactive demo (default)")
    group.add_argument("--run-tests", action="store_true", help="Run the test suite using pytest")
    parser.add_argument(
        "--module",
        type=str,
        help=(
            "Run a specific module demo: primitive,type_casting,classes,dunder,"
            "data_structures,introspection"
        ),
    )
    parser.add_argument("--quiet", action="store_true", help="Run with minimal output")
    return parser.parse_args()


def _run_pytest(quiet: bool = False) -> int:
    """Run the project's tests using pytest.

    Returns the exit code from the pytest subprocess.
    """
    cmd = [sys.executable, "-m", "pytest", "tests/", "-v"]
    if quiet:
        cmd = [sys.executable, "-m", "pytest", "tests/", "-q"]
    return subprocess.call(cmd)


def main(args: Optional[argparse.Namespace] = None) -> int:
    """Main entry point for demonstrations or test runner.

    Args:
        args: Parsed arguments (if None, will parse from sys.argv).

    Returns:
        Exit code integer.
    """
    if args is None:
        args = parse_args()

    # Run tests if requested
    if args.run_tests:
           return _run_pytest(quiet=args.quiet)

    # Demo flow
    target = (args.module or "").lower()

    print("=" * 70)
    print("PYTHON TRAINING - COMPREHENSIVE DEMONSTRATIONS")
    print("=" * 70)

    # Primitive Data Types
    if not target or target in ("primitive", "primitive_datatypes"):
        print("\n1. PRIMITIVE DATA TYPES")
        print("-" * 70)
        manager = PrimitiveManager()
        int_demo = manager.get_integer_demonstrations()
        print(f"Integer operations: {int_demo['basic_operations']}")

    # Type Casting
    if not target or target == "type_casting":
        print("\n2. TYPE CASTING")
        print("-" * 70)
        print(f"Safe int casting: {SafeCast.to_int('42')} (from '42')")
        print(f"Numeric casting: {NumericCasting.int_to_float()}")

    # Classes and Objects
    if not target or target == "classes":
        print("\n3. OBJECT-ORIENTED PROGRAMMING")
        print("-" * 70)
        class_mgr = ClassManager()
        demo_data = class_mgr.get_demo_data()
        print(f"Total students: {len(demo_data['students'])}")
        print(f"Total employees: {len(demo_data['employees'])}")

    # Dunder Methods
    if not target or target == "dunder":
        print("\n4. OPERATOR OVERLOADING (DUNDER METHODS)")
        print("-" * 70)
        num1 = CustomNumber(10)
        num2 = CustomNumber(5)
        print(f"CustomNumber(10) + CustomNumber(5) = {(num1 + num2).value}")
        str1 = CustomString("Hello")
        str2 = CustomString(" World")
        print(f"CustomString('Hello') + CustomString(' World') = '{(str1 + str2).value}'")

    # Data Structures
    if not target or target in ("data_structures", "lists", "tuples", "sets", "dictionaries"):
        print("\n5. DATA STRUCTURE OPERATIONS")
        print("-" * 70)
        list_ops = ListManager.basic_operations()
        print(f"List operations: {list_ops['length']} elements")
        set_ops = SetManager.set_operations()
        print(f"Set union: {set_ops['union']}")
        dict_ops = DictionaryManager.basic_operations()
        print(f"Dictionary operations: {dict_ops['length']} keys")

    # Introspection
    if not target or target == "introspection":
        print("\n6. INTROSPECTION & REFLECTION")
        print("-" * 70)
        obj_info = ObjectInspector.inspect_object([1, 2, 3])
        print(f"Object type: {obj_info['type']}")
        print(f"Object ID: {obj_info['id']}")

    print("\n" + "=" * 70)
    print("TRAINING MODULES OVERVIEW")
    print("=" * 70)
    print("""
    This comprehensive Python training includes:
    
    1. Primitive Data Types:
       - Integers, Floats, Strings, Booleans
       - Operations, methods, and best practices
    
    2. Type Casting:
       - Safe casting with error handling
       - Numeric, string, and boolean conversions
    
    3. Introspection:
       - Object inspection (dir, isinstance, type)
       - Documentation access and analysis
    
    4. Object-Oriented Programming:
       - Classes, inheritance, and composition
       - Instance and class methods
    
    5. Dunder Methods:
       - Operator overloading
       - Custom string and number implementations
    
    6. Data Structures:
       - Lists, tuples, sets, dictionaries
       - Comprehensive methods and operations
    
    Run tests with: python -m pytest tests/
    """)

    return 0


if __name__ == "__main__":
    args = parse_args()
    sys.exit(main(args))
