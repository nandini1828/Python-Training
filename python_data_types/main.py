"""
Python Data Types - Master Demo Runner

Covers:
- Introspection
- Dunder Methods
- Truthiness
- Type Checking & Casting
- Lists
- Sets
- Dictionaries
"""

import argparse

# =========================================================
# IMPORTS
# =========================================================

# Introspection
from introspection import (
    get_type,
    get_id,
    get_public_attributes,
)
from introspection.models import Dog

# Dunder
from dunder.operators import Box

# Truthiness
from truthiness.evaluator import count_truthy_falsy

# Type Checking & Casting
from type_checking_casting.checker import check_type
from type_checking_casting.casting import safe_cast

# Lists
from lists.simple_queue import SimpleQueue

# Sets
from sets import merge_tags

# Dictionaries
from dictionaries.dictionary_methods import safe_get
from dictionaries.vocabulary import word_count
from dictionaries.json_query import query_json

# =========================================================
# ARGPARSE CONFIGURATION
# =========================================================

parser = argparse.ArgumentParser(
    description="Python Data Types Demonstration"
)

parser.add_argument(
    "--module",
    choices=[
        "introspection",
        "dunder",
        "truthiness",
        "types",
        "lists",
        "sets",
        "dicts",
        "all",
    ],
    default="all",
    help="Choose which module demo to execute.",
)

# =========================================================
# DEMO FUNCTIONS
# =========================================================

def run_introspection_demo():
    print("\n========== INTROSPECTION ==========")

    dog = Dog()

    print("Type:", get_type(dog))
    print("ID:", get_id(dog))
    print("Public Attributes:", get_public_attributes(dog))


def run_dunder_demo():
    print("\n========== DUNDER METHODS ==========")

    box1 = Box(10)
    box2 = Box(20)

    print("box1 + box2 =", box1 + box2)
    print("box1 == box2 =", box1 == box2)
    print("str(box1) =", str(box1))
    print("repr(box1) =", repr(box1))


def run_truthiness_demo():
    print("\n========== TRUTHINESS ==========")

    values = [0, "hello", [], None, True, 3.14]

    result = count_truthy_falsy(values)

    print("Truthy :", result["truthy"])
    print("Falsy  :", result["falsy"])


def run_type_demo():
    print("\n========== TYPE CHECKING & CASTING ==========")

    print("check_type(10, int):", check_type(10, int))
    print("safe_cast('10', int):", safe_cast("10", int))
    print("safe_cast('abc', int, 0):", safe_cast("abc", int, 0))


def run_list_demo():
    print("\n========== LISTS ==========")

    queue = SimpleQueue()

    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    print("Dequeued :", queue.dequeue())
    print("Queue Size:", queue.size())


def run_set_demo():
    print("\n========== SETS ==========")

    tags_a = ["Python", "AI", "ML"]
    tags_b = ["ai", "data", "ml"]

    unique, shared, only_a = merge_tags(tags_a, tags_b)

    print("Unique :", unique)
    print("Shared :", shared)
    print("Only A :", only_a)


def run_dictionary_demo():
    print("\n========== DICTIONARIES ==========")

    print("Safe Get:", safe_get({"a": 1}, "a"))

    sentence = "Hello hello world"

    print("Word Count:", word_count(sentence))

    data = {
        "user": {
            "profile": {
                "name": "Indiana Jones"
            }
        }
    }

    print(
        "JSON Query:",
        query_json(data, "user.profile.name")
    )


def run_all_demos():
    """
    Executes every demonstration module.
    """
    run_introspection_demo()
    run_dunder_demo()
    run_truthiness_demo()
    run_type_demo()
    run_list_demo()
    run_set_demo()
    run_dictionary_demo()


# =========================================================
# MODULE ROUTER
# =========================================================

MODULES = {
    "introspection": run_introspection_demo,
    "dunder": run_dunder_demo,
    "truthiness": run_truthiness_demo,
    "types": run_type_demo,
    "lists": run_list_demo,
    "sets": run_set_demo,
    "dicts": run_dictionary_demo,
    "all": run_all_demos,
}

# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":
    args = parser.parse_args()

    MODULES[args.module]()