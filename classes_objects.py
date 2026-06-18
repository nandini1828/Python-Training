# Class and Object
class Student:
    pass
student1 = Student()
student2 = Student()

# Creating attributes
class Student:
    pass
student1 = Student()
student1.name = "Nandini"
student1.age = 20
print(student1.name)
print(student1.age)

# Constructor (__init__)
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Nandini", 20)
print(student1.name)
print(student1.age)

# Multiple objects
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Nandini", 20)
student2 = Student("Rahul", 21)
print(student1.name)
print(student2.name)

# Instance method
class Student:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)
student1 = Student("Nandini")
student1.display()

# Using multiple attributes in methods
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def details(self):
        print(self.name)
        print(self.age)
student1 = Student("Nandini", 20)
student1.details()

# Static method
class Calculator:
    @staticmethod
    def add(a, b):
        print(a + b)
Calculator.add(10, 20)

# Constructor with default value
class Student:
    def __init__(self, name, age=20):
        self.name = name
        self.age = age
student1 = Student("Nandini")
print(student1.name)
print(student1.age)

# Object as parameter
class Student:
    def __init__(self, name):
        self.name = name
def show(student):
    print(student.name)
student1 = Student("Nandini")
show(student1)

# Destructor
class Student:
    def __del__(self):
        print("Object Destroyed")
student1 = Student()
del student1

# Bank account example
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def display_balance(self):
        print(self.balance)
account1 = BankAccount("Nandini", 10000)
account1.deposit(5000)
account1.withdraw(2000)
account1.display_balance()