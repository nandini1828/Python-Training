"""
==================================================
Module: List Utilities
Topic: Python List Methods
Author: Nandini

Description:
Demonstrates commonly used Python list methods.
==================================================
"""


def demonstrate_list_methods():
    """
    Demonstrates important list methods.

    Returns:
        None
    """

    print("\n========== LIST METHODS ==========\n")

    # ----------------------------------------
    # append()
    # ----------------------------------------

    students = ["Nandini", "Rahul"]

    print("Original List:", students)

    students.append("Priya")

    print("\nappend('Priya')")
    print(students)

    # ----------------------------------------
    # extend()
    # ----------------------------------------

    students.extend(["Kiran", "Aman"])

    print("\nextend(['Kiran', 'Aman'])")
    print(students)

    # ----------------------------------------
    # insert()
    # ----------------------------------------

    students.insert(1, "Suresh")

    print("\ninsert(1, 'Suresh')")
    print(students)

    # ----------------------------------------
    # remove()
    # ----------------------------------------

    students.remove("Rahul")

    print("\nremove('Rahul')")
    print(students)

    # ----------------------------------------
    # pop()
    # ----------------------------------------

    removed_student = students.pop()

    print("\npop()")
    print("Removed:", removed_student)
    print(students)

    # ----------------------------------------
    # index()
    # ----------------------------------------

    print("\nindex('Priya')")
    print(students.index("Priya"))

    # ----------------------------------------
    # count()
    # ----------------------------------------

    numbers = [1, 2, 2, 3, 2, 4]

    print("\ncount(2)")
    print(numbers.count(2))

    # ----------------------------------------
    # sort()
    # ----------------------------------------

    marks = [78, 92, 45, 88, 67]

    marks.sort()

    print("\nsort()")
    print(marks)

    # ----------------------------------------
    # reverse()
    # ----------------------------------------

    marks.reverse()

    print("\nreverse()")
    print(marks)

    # ----------------------------------------
    # copy()
    # ----------------------------------------

    copied_marks = marks.copy()

    print("\ncopy()")
    print(copied_marks)

    # ----------------------------------------
    # clear()
    # ----------------------------------------

    copied_marks.clear()

    print("\nclear()")
    print(copied_marks)

    print("\n===================================")