def sort_students(students):

    print("\nStudents Sorted By Average")

    sorted_students = sorted(
        students,
        key=lambda student: student.average(),
        reverse=True
    )

    for student in sorted_students:
        print(student.name, student.average())