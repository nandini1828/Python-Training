"""
Section 5: Classes, Composition & self
"""


class CPU:

    def __init__(self, cores):
        self.cores = cores


class Computer:

    def __init__(self, brand, cpu):
        self.brand = brand
        self.cpu = cpu


class Student:

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


def demonstrate_self():

    student = Student(
        "Vyshu",
        [90, 95, 85]
    )

    return student.average_grade()


def demonstrate_composition():

    computer = Computer(
        "Dell",
        CPU(8)
    )

    return {
        "computer_dict": computer.__dict__,
        "cpu_dict": computer.cpu.__dict__
    }


def inspect_instance_memory(obj):
    """
    Returns the instance dictionary.
    """

    return obj.__dict__