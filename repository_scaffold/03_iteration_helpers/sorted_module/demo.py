"""
demo.py

Practical demonstrations of Python's built-in sorted() function.

Run:
    python demo.py
"""


def sort_numbers():
    print("\n===== Sort Numbers =====")

    numbers = [45, 12, 78, 23, 9]

    print("Original :", numbers)
    print("Sorted   :", sorted(numbers))


def sort_descending():
    print("\n===== Descending Order =====")

    numbers = [45, 12, 78, 23, 9]

    print(sorted(numbers, reverse=True))


def sort_strings():
    print("\n===== Sort Strings =====")

    fruits = ["Orange", "Apple", "Mango", "Banana"]

    print(sorted(fruits))


def sort_by_length():
    print("\n===== Sort By Length =====")

    names = ["Ganesh", "Raj", "Christopher", "Priya"]

    print(sorted(names, key=len))


def sort_dictionary_keys():
    print("\n===== Sort Dictionary Keys =====")

    student = {
        "course": "Python",
        "name": "Ganesh",
        "age": 22,
    }

    print(sorted(student))


def sort_dictionary_items():
    print("\n===== Sort Dictionary Items =====")

    marks = {
        "Ganesh": 95,
        "Rahul": 88,
        "Priya": 91,
    }

    for name, mark in sorted(marks.items()):
        print(name, mark)


def sort_tuples():
    print("\n===== Sort Tuples =====")

    coordinates = [
        (3, 4),
        (1, 8),
        (2, 5),
    ]

    print(sorted(coordinates))


def sort_students_by_marks():
    print("\n===== Sort Students By Marks =====")

    students = [
        ("Ganesh", 95),
        ("Rahul", 88),
        ("Priya", 91),
    ]

    sorted_students = sorted(
        students,
        key=lambda student: student[1],
        reverse=True,
    )

    for student in sorted_students:
        print(student)


def case_insensitive_sort():
    print("\n===== Case-Insensitive Sort =====")

    languages = ["python", "Java", "c", "Go"]

    print(sorted(languages, key=str.lower))


def preserve_original():
    print("\n===== Preserve Original List =====")

    values = [5, 1, 8, 3]

    sorted_values = sorted(values)

    print("Original :", values)
    print("Sorted   :", sorted_values)


def main():
    print("=" * 70)
    print("SORTED() FUNCTION DEMONSTRATIONS")
    print("=" * 70)

    sort_numbers()
    sort_descending()
    sort_strings()
    sort_by_length()
    sort_dictionary_keys()
    sort_dictionary_items()
    sort_tuples()
    sort_students_by_marks()
    case_insensitive_sort()
    preserve_original()

    print("\nAll demonstrations completed successfully.")


if __name__ == "__main__":
    main()