#List

"""
Shopping Cart System

Manage products selected by customers.
"""

cart = []

# Add products
cart.append("Laptop")
cart.append("Mouse")

# Add multiple products
cart.extend(
    ["Keyboard", "Monitor"]
)

# Insert priority product
cart.insert(1, "Headphones")

print(cart)

# Remove product
cart.remove("Mouse")

# Remove last product
removed_product = cart.pop()

print(f"Removed: {removed_product}")

# Sort products alphabetically
cart.sort()

print(cart)

#Tuple

"""
Location Tracking

Coordinates should never change.
"""

office_location = (
    17.3850,
    78.4867
)

print(office_location)

print(
    office_location.index(78.4867)
)

#Set
"""
Skill Management System

Prevent duplicate skills.
"""

skills = {
    "Python",
    "AWS",
    "Docker"
}

skills.add("Kubernetes")

# Duplicate ignored automatically
skills.add("Python")

print(skills)

#Dictionary
"""
Employee Information System

Store employee details.
"""

employee = {
    "employee_id": 101,
    "name": "John Smith",
    "department": "Engineering"
}

print(
    employee.get("department")
)

employee.update(
    {"department": "AI Engineering"}
)

print(employee)

print(employee.keys())
print(employee.values())

