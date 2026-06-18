# This file demonstrates basic OOP concepts.


# 1) Class and Object
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print(f"Brand: {self.brand}, Price: ₹{self.price}")


# 2) Inheritance
class SmartPhone(Mobile):
    def __init__(self, brand, price, camera):
        super().__init__(brand, price)
        self.camera = camera

    def show_camera(self):
        print(f"{self.brand} has a {self.camera}MP camera")


# 3) Polymorphism
class Car:
    def start(self):
        print("Car starts with a key")


class ElectricCar:
    def start(self):
        print("Electric car starts with a button")


# 4) Encapsulation
class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def add_money(self, amount):
        self.__balance += amount
        print(f"Added ₹{amount}")

    def show_balance(self):
        print(f"Current Balance: ₹{self.__balance}")


# 5) Abstraction
class Vehicle:
    def move(self):
        pass


class Bike(Vehicle):
    def move(self):
        print("Bike is moving")


# Example Usage
if __name__ == "__main__":

    print("=== Class and Object ===")
    mobile1 = Mobile("Samsung", 50000)
    mobile1.display()

    print("\n=== Inheritance ===")
    phone1 = SmartPhone("iPhone", 80000, 48)
    phone1.display()
    phone1.show_camera()

    print("\n=== Polymorphism ===")
    for vehicle in (Car(), ElectricCar()):
        vehicle.start()

    print("\n=== Encapsulation ===")
    wallet = Wallet("Bhavya", 1000)
    wallet.show_balance()
    wallet.add_money(500)
    wallet.show_balance()

    print("\n=== Abstraction ===")
    bike = Bike()
    bike.move()