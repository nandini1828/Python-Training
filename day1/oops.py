"""Understanding OOP (Object-Oriented Programming)
OOP is a way of designing software using Objects and Classes."""

"""Class -> A Class is a blueprint/template."""

"""Object -> An Object is a real instance created from a class."""

# Four Pillars of OOP
# 1. Encapsulation -> Wrapping data and methods into a single unit (class)
# 2. Abstraction -> Hiding the internal details and showing only the functionality
# 3. Inheritance -> Acquiring properties and behaviors of another class
# 4. Polymorphism -> Ability to take many forms (same method name but different behavior)


# ENCAPSULATION
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
print(account.get_balance())

# ABSTRACTION   
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car Started")
car = Car()
car.start() 

# INHERITANCE
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} is barking")
dog = Dog("Buddy")
dog.eat()

# POLYMORPHISM
class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()





