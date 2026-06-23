"""
==================================================
Module: Dictionary Utilities
Topic: Python Dictionary Methods
Author: Nandini

Description:
Demonstrates commonly used dictionary methods.
==================================================
"""


def demonstrate_dictionary_methods():
    """
    Demonstrates important dictionary methods.

    Returns:
        None
    """

    print("\n========== DICTIONARY METHODS ==========\n")

    student = {
        "name": "Nandini",
        "age": 21,
        "branch": "CSE-DS"
    }

    print("Original Dictionary:")
    print(student)

    # ----------------------------------------
    # keys()
    # ----------------------------------------

    print("\nkeys()")
    print(student.keys())

    # ----------------------------------------
    # values()
    # ----------------------------------------

    print("\nvalues()")
    print(student.values())

    # ----------------------------------------
    # items()
    # ----------------------------------------

    print("\nitems()")
    print(student.items())

    # ----------------------------------------
    # update()
    # ----------------------------------------

    student.update({"cgpa": 9.15})

    print("\nupdate({'cgpa': 9.15})")
    print(student)

    # ----------------------------------------
    # pop()
    # ----------------------------------------

    removed_value = student.pop("age")

    print("\npop('age')")
    print("Removed:", removed_value)
    print(student)

    # ----------------------------------------
    # popitem()
    # ----------------------------------------

    removed_item = student.popitem()

    print("\npopitem()")
    print("Removed:", removed_item)
    print(student)

    # ----------------------------------------
    # copy()
    # ----------------------------------------

    copied_student = student.copy()

    print("\ncopy()")
    print(copied_student)

    # ----------------------------------------
    # clear()
    # ----------------------------------------

    copied_student.clear()

    print("\nclear()")
    print(copied_student)

    # ----------------------------------------
    # fromkeys()
    # ----------------------------------------

    subjects = ["Python", "Java", "SQL"]

    marks = dict.fromkeys(subjects, 0)

    print("\nfromkeys(subjects, 0)")
    print(marks)

    print("\n========================================")