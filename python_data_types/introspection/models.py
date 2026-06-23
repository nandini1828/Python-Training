class Animal:
    """Base class representing an animal."""

    def eat(self):
        """Animal eats food."""
        return "Eating..."


class Dog(Animal):
    """Dog class inherits Animal."""

    def bark(self):
        """Dog makes sound."""
        return "Woof!"


class Student:
    """Represents a student."""

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        """Returns average marks."""
        return sum(self.marks) / len(self.marks)