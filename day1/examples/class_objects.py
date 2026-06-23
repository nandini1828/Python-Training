from day1.models.student import Student

def main():

    student = Student(
        name="Karthik",
        marks=85,
        grade="A"
    )

    student.display_information()


if __name__ == "__main__":
    main()