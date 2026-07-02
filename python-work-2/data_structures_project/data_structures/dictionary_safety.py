"""
Dictionary safety.
"""

from collections import defaultdict


def get_demo():

    student = {
        "name": "Alice"
    }

    print(student.get("name"))
    print(student.get("age"))
    print(student.get("age", 0))


def defaultdict_demo():

    marks = defaultdict(int)

    marks["Math"] += 10
    marks["Science"] += 20

    print(dict(marks))


def demo():

    get_demo()
    defaultdict_demo()