def display_students(students):

    print("\nStudent Attendance")

    for roll, student in enumerate(students, start=1):
        print(f"{roll}. {student.name}")