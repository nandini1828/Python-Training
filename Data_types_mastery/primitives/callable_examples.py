# callable() checks whether an object can be called using parentheses ().
"""
Callable Examples
"""

def greet():
    """
    Prints greeting.
    """
    print("Hello")


class Student:

    def get_name(self):
        """
        Returns student name.
        """
        return "Karthik"


def demonstrate_callable():

    print(
        callable(greet)
    )

    print(
        callable(Student)
    )

    student = Student()

    print(
        callable(student)
    )

    print(
        callable(
            student.get_name
        )
    )


if __name__ == "__main__":
    demonstrate_callable()