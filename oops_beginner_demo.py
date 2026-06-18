# This file shows simple OOP ideas using easy examples.

# 1) Class and object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# 2) Inheritance
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def show_grade(self):
        print(f"{self.name} has grade {self.grade}")


# 3) Polymorphism
class Dog:
    def sound(self):
        print("Dog says: bow bow")


class Cat:
    def sound(self):
        print("Cat says: meow")


# 4) Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. Balance is {self.__balance}")

    def show_balance(self):
        print(f"{self.owner} has {self.__balance} in the account")


# 5) Abstraction
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Example usage
if __name__ == "__main__":
    print("=== Class and Object ===")
    person1 = Person("Asha", 21)
    person1.greet()

    print("\n=== Inheritance ===")
    student1 = Student("Ravi", 20, 85)
    student1.show_grade()

    print("\n=== Polymorphism ===")
    for animal in (Dog(), Cat()):
        animal.sound()

    print("\n=== Encapsulation ===")
    account = BankAccount("Vishnu", 100)
    account.show_balance()
    account.deposit(50)
    account.show_balance()

    print("\n=== Abstraction ===")
    rect = Rectangle(5, 4)
    print("Rectangle area:", rect.area())
