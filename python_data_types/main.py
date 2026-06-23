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

# INTROSPECTION

from introspection import get_type, get_id, get_public_attributes
from introspection.models import Dog


# DUNDER METHODS

from dunder.operators import Box

# TRUTHINESS
from truthiness.evaluator import count_truthy_falsy


# TYPE CHECKING & CASTING
from type_checking_casting.checker import check_type
from type_checking_casting.casting import safe_cast

# LISTS

from lists.simple_queue import SimpleQueue

# SETS
from sets import merge_tags, union_sets

# DICTIONARIES

from dictionaries.dictionary_methods import safe_get
from dictionaries.vocabulary import word_count
from dictionaries.json_query import query_json

# MAIN EXECUTION


def run_introspection_demo():
    print("\n===== INTROSPECTION =====")

    dog = Dog()

    print("Type:", get_type(dog))
    print("ID:", get_id(dog))
    print("Public Attributes:", get_public_attributes(dog))


def run_dunder_demo():
    print("\n===== DUNDER METHODS =====")

    a = Box(10)
    b = Box(20)

    print("a + b =", a + b)
    print("a == b =", a == b)
    print("str(a) =", str(a))
    print("repr(a) =", repr(a))


def run_truthiness_demo():
    print("\n===== TRUTHINESS =====")

    data = [0, "hello", [], None, True, 3.14]
    result = count_truthy_falsy(data)

    print("Truthy:", result["truthy"])
    print("Falsy:", result["falsy"])


def run_type_demo():
    print("\n===== TYPE CHECKING & CASTING =====")

    print(check_type(10, int))

    print("Safe Cast int:", safe_cast("10", int))
    print("Safe Cast fail:", safe_cast("abc", int, 0))


def run_list_demo():
    print("\n===== LISTS (QUEUE) =====")

    q = SimpleQueue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")

    print("Dequeued:", q.dequeue())
    print("Size:", q.size())


def run_set_demo():
    print("\n===== SETS =====")

    tags_a = ["Python", "AI", "ML"]
    tags_b = ["ai", "data", "ml"]

    unique, shared, only_a = merge_tags(tags_a, tags_b)

    print("Unique:", unique)
    print("Shared:", shared)
    print("Only A:", only_a)


def run_dict_demo():
    print("\n===== DICTIONARIES =====")

    print("Safe Get:", safe_get({"a": 1}, "a"))

    text = "Hello hello world"
    print("Word Count:", word_count(text))

    data = {"user": {"profile": {"name": "Indiana Jones"}}}
    print("JSON Query:", query_json(data, "user.profile.name"))


# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":
    run_introspection_demo()
    run_dunder_demo()
    run_truthiness_demo()
    run_type_demo()
    run_list_demo()
    run_set_demo()
    run_dict_demo()