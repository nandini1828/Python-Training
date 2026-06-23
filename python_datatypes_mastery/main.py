"""
Demo application for python_datatypes_mastery.

This script runs concise demonstrations of the modules in the package.
"""
from __future__ import annotations

from primitives.introspection import inspect_object
from primitives.casting import safe_cast
from primitives.dunder_examples import Employee, demo_dunders
from collections.list_utils import demo_list_methods
from collections.dict_utils import demo_dict_methods
from collections.set_utils import demo_set_methods
from classes.student import Student
from classes.computer import CPU, Computer
from classes.object_deconstructor import deconstruct_object
from inspectors.method_inspector import get_methods_and_docs
from exercises.queue import SimpleQueue
from exercises.json_query import query_json


def run_demo() -> None:
    """Run a short, readable demonstration for learners.

    The function prints results of selected utilities to the console.
    """
    print("--- Introspection ---")
    sample = [1, "two", {"three": 3}]
    print(inspect_object(sample))

    print("\n--- Casting ---")
    print(safe_cast("123", int, default=0))
    print(safe_cast("bad", int, default=-1))

    print("\n--- Dunder Methods ---")
    emp_a = Employee("Alice", salary=70000)
    emp_b = Employee("Bob", salary=50000)
    print(emp_a + emp_b)
    print(repr(emp_a))
    demo_dunders()

    print("\n--- Lists / Dicts / Sets ---")
    print(demo_list_methods([1, 2, 3], [4, 5]))
    print(demo_dict_methods({"a": 1}, {"b": 2}))
    print(demo_set_methods({1, 2}, {2, 3}))

    print("\n--- Classes & Composition ---")
    student = Student("Charlie", [88, 92, 75])
    print(student.__dict__)
    print("Average (unbound):", Student.average_grade(student))

    cpu = CPU(cores=4, frequency_ghz=3.2)
    computer = Computer(brand="ExampleBrand", cpu=cpu)
    print(computer.__dict__)

    print("\n--- Object Deconstruction ---")
    print(deconstruct_object(computer))

    print("\n--- Inspectors ---")
    print(get_methods_and_docs([]))

    print("\n--- Queue & JSON Query ---")
    q = SimpleQueue()
    q.enqueue(10)
    q.enqueue(20)
    print("Queue size:", q.size())
    print("Dequeue:", q.dequeue())

    data = {"user": {"profile": {"name": "Dana"}}}
    print(query_json(data, "user.profile.name"))


if __name__ == "__main__":
    run_demo()
