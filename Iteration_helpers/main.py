"""Student Marks Report"""


def build_students():
    """Create a list of student records."""
    names = ["Asha", "Ravi", "Meera", "John"]
    marks = [88, 72, 95, 41]
    return list(zip(names, marks))


def show_roll_numbers(students):
    """Use range() and enumerate() to display roll numbers."""
    for index, student in enumerate(students, start=1):
        print(f"Roll {index}: {student[0]} -> {student[1]}")


def pair_names_with_marks(names, marks):
    """Use zip() to pair names with marks."""
    return list(zip(names, marks))


def sort_students(students):
    """Sort students by marks."""
    return sorted(students, key=lambda item: item[1])


def reverse_students(students):
    """Reverse the student order."""
    return list(reversed(students))


def check_results(students):
    """Use any() and all() to summarize results."""
    any_failed = any(mark < 50 for _, mark in students)
    all_passed = all(mark >= 50 for _, mark in students)
    return any_failed, all_passed


def main():
    print("Student Marks Report")
    students = build_students()

    print("\nRoll numbers and students:")
    show_roll_numbers(students)

    names = [name for name, _ in students]
    marks = [mark for _, mark in students]
    paired = pair_names_with_marks(names, marks)
    print("\nPaired names and marks:", paired)

    print("\nSorted by marks:", sort_students(students))
    print("\nReversed order:", reverse_students(students))

    any_failed, all_passed = check_results(students)
    print(f"\nAnyone failed? {any_failed}")
    print(f"Everyone passed? {all_passed}")


if __name__ == "__main__":
    main()
