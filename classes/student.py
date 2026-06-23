class Student:
    """Represents a student with a name and a list of numeric grades."""

    def __init__(self, name, grades):
        """Initialize a Student with a name and grades list."""
        self.name = name
        self.grades = grades

    def average_grade(self):
        """Return the average of the stored grades."""
        return sum(self.grades) / len(self.grades)
