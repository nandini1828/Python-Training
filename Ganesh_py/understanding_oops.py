# understanding_oops.py

from abc import ABC, abstractmethod

def run():
    title = "Understanding OOPS"
    description = "Explains encapsulation, inheritance, polymorphism, and abstraction with examples."

    class BankAccount:
        def __init__(self, account_holder, balance):
            self.__account_holder = account_holder
            self.__balance = balance

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
                return f"Deposited: ${amount}"
            return "Invalid amount"

        def withdraw(self, amount):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                return f"Withdrawn: ${amount}"
            return "Insufficient funds or invalid amount"

        def get_balance(self):
            return self.__balance

    class Vehicle:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

        def display_info(self):
            return f"{self.brand} {self.model}"

        def start(self):
            return "Engine started"

    class Car(Vehicle):
        def __init__(self, brand, model, doors):
            super().__init__(brand, model)
            self.doors = doors

        def display_info(self):
            return f"{self.brand} {self.model} ({self.doors} doors)"

        def open_trunk(self):
            return "Trunk opened"

    class Motorcycle(Vehicle):
        def __init__(self, brand, model, has_sidecar):
            super().__init__(brand, model)
            self.has_sidecar = has_sidecar

        def wheelie(self):
            return "Performing a wheelie!"

    class Animal(ABC):
        @abstractmethod
        def speak(self):
            pass

    class Dog(Animal):
        def speak(self):
            return "Woof! Woof!"

    class Cat(Animal):
        def speak(self):
            return "Meow! Meow!"

    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

        @abstractmethod
        def perimeter(self):
            pass

        def describe(self):
            return f"This is a {self.__class__.__name__}"

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius ** 2

        def perimeter(self):
            return 2 * 3.14 * self.radius

    class Rectangle(Shape):
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area(self):
            return self.length * self.width

        def perimeter(self):
            return 2 * (self.length + self.width)

    account = BankAccount("John", 1000)
    vehicle = Car("Toyota", "Camry", 4)
    bike = Motorcycle("Harley-Davidson", "Sportster", False)
    dog = Dog()
    cat = Cat()
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    details = [
        "### Encapsulation",
        account.deposit(500),
        account.withdraw(200),
        f"balance = {account.get_balance()}",
        "",
        "### Inheritance",
        vehicle.display_info(),
        vehicle.start(),
        vehicle.open_trunk(),
        bike.display_info(),
        bike.wheelie(),
        "",
        "### Polymorphism",
        dog.speak(),
        cat.speak(),
        "",
        "### Abstraction",
        circle.describe(),
        f"circle area = {circle.area()}",
        f"circle perimeter = {circle.perimeter()}",
        rectangle.describe(),
        f"rectangle area = {rectangle.area()}",
        f"rectangle perimeter = {rectangle.perimeter()}",
    ]

    return {
        "title": title,
        "description": description,
        "details": "\n".join(details),
    }


if __name__ == "__main__":
    result = run()
    print(result["title"])
    print(result["description"])
    print(result["details"])
