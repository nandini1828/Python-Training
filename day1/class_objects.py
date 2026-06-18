class Laptop:
    """
    Represents a Laptop object.
    """

    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def upgrade_ram(self, new_ram):
        self.ram = new_ram

    def apply_discount(self, discount):
        self.price -= discount

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram} GB")
        print(f"Price: ₹{self.price}")

    def __str__(self):
        return f"{self.brand} | {self.ram}GB | ₹{self.price}"


# Creating Objects
laptop1 = Laptop("Dell", 8, 50000)
laptop2 = Laptop("HP", 16, 65000)
laptop3 = Laptop("Lenovo", 32, 80000)

# Accessing Object Variables
print(laptop1.brand)
print(laptop2.price)

# Calling Methods
laptop1.upgrade_ram(16)
laptop2.apply_discount(5000)

# Display Details
laptop1.display_details()

# Using __str__
print(laptop1)
print(laptop2)
print(laptop3)