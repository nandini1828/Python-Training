"""Example programs for OOP concepts: encapsulation, inheritance, polymorphism, abstraction."""

from abc import ABC, abstractmethod


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # private attribute

    def get_salary(self):
        return self.__salary


class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Bird:
    def move(self):
        print("Bird flies")


class Fish:
    def move(self):
        print("Fish swims")


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


def demo():
    print("Encapsulation demo:")
    employee = Employee("Vamshi", 50000)
    print("Salary (via getter):", employee.get_salary())
    print()

    print("Inheritance demo:")
    dog = Dog()
    dog.sound()
    dog.bark()
    print()

    print("Polymorphism demo:")
    for obj in (Bird(), Fish()):
        obj.move()
    print()

    print("Abstraction demo:")
    square = Square(5)
    print("Square area:", square.area())


if __name__ == "__main__":
    demo()
