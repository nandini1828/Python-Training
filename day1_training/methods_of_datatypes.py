#String Methods
"""
Employee Registration System
Demonstrates important String methods.
"""

employee_name = "  venkatesh kumar  "
employee_email = "VENKATESH@GMAIL.COM"

# strip() -> Removes leading and trailing spaces
employee_name = employee_name.strip()

# title() -> Capitalizes first letter of every word
employee_name = employee_name.title()

# lower() -> Converts to lowercase
employee_email = employee_email.lower()

print("Employee Name :", employee_name)
print("Employee Email:", employee_email)

# startswith()
if employee_email.startswith("venkatesh"):
    print("Email belongs to Venkatesh")

# endswith()
if employee_email.endswith(".com"):
    print("Valid domain")

# replace()
official_email = employee_email.replace("@gmail.com", "@company.com")
print("Official Email:", official_email)

# split()
first_name, last_name = employee_name.split()
print("First Name:", first_name)
print("Last Name :", last_name)

# join()
employee_id = "-".join(["EMP", "101"])
print("Employee ID:", employee_id)

# find()
position = official_email.find("@")
print("@ found at index:", position)

# isalpha()
print("First Name Contains Only Letters:", first_name.isalpha())

# upper()
print("Upper Case Name:", employee_name.upper())

# lower()
print("Lower Case Name:", employee_name.lower())

# count()
print("Letter 'a' Count:", employee_name.lower().count("a"))

# len()
print("Total Characters:", len(employee_name))

#List Methods

"""
Shopping Cart System
Demonstrates important List methods.
"""

cart = []

# append()
cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print("Cart:", cart)

# insert()
cart.insert(1, "Headphones")
print("After Insert:", cart)

# extend()
cart.extend(["Monitor", "USB Cable"])
print("After Extend:", cart)

# count()
print("Laptop Count:", cart.count("Laptop"))

# index()
print("Keyboard Position:", cart.index("Keyboard"))

# remove()
cart.remove("Mouse")
print("After Removing Mouse:", cart)

# pop()
removed_item = cart.pop()
print("Removed Item:", removed_item)

# sort()
prices = [50000, 1000, 2500, 15000]
prices.sort()
print("Sorted Prices:", prices)

# reverse()
prices.reverse()
print("Descending Prices:", prices)

# copy()
backup_cart = cart.copy()
print("Backup Cart:", backup_cart)

# clear()
temp_cart = cart.copy()
temp_cart.clear()
print("Temporary Cart:", temp_cart)

# len()
print("Total Items:", len(cart))

# membership operator
if "Laptop" in cart:
    print("Laptop Available")

#Dictionary Methods

"""
Student Management System
Demonstrates important Dictionary methods.
"""

student = {
    "id": 101,
    "name": "Venkatesh",
    "course": "Python"
}

print("Student Data:", student)

# get()
print("Student Name:", student.get("name"))

# update()
student.update({"course": "AI Engineering"})
print("After Update:", student)

# keys()
print("Keys:")
for key in student.keys():
    print(key)

# values()
print("\nValues:")
for value in student.values():
    print(value)

# items()
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, "->", value)

# setdefault()
student.setdefault("city", "Hyderabad")
print("\nAfter setdefault:", student)

# pop()
removed = student.pop("city")
print("Removed:", removed)

# popitem()
last_item = student.popitem()
print("Last Removed Item:", last_item)

# copy()
student_backup = student.copy()
print("Backup:", student_backup)

# fromkeys()
subjects = dict.fromkeys(
    ["Python", "Java", "SQL"],
    "Not Started"
)
print("Subjects:", subjects)

# clear()
temp = student.copy()
temp.clear()
print("Cleared Dictionary:", temp)

# Membership
if "name" in student:
    print("Name Key Exists")

# Tuple Methods

"""
Employee Records System
Demonstrates important Tuple methods.
"""

# Tuple is immutable
employee = (
    101,
    "Venkatesh",
    "Python Developer",
    "Hyderabad"
)

print("Employee Record:", employee)

# Accessing elements
print("Employee ID:", employee[0])
print("Employee Name:", employee[1])

# count()
sample_data = (10, 20, 30, 10, 40, 10)
print("Count of 10:", sample_data.count(10))

# index()
print("Position of 30:", sample_data.index(30))

# len()
print("Total Elements:", len(employee))

# Slicing
print("Basic Details:", employee[:2])

# Iteration
print("\nEmployee Details:")
for detail in employee:
    print(detail)

# Membership
if "Python Developer" in employee:
    print("Employee is a Python Developer")

# Tuple Packing
packed_data = (101, "Venkatesh", 75000)

# Tuple Unpacking
emp_id, emp_name, salary = packed_data

print("\nTuple Unpacking")
print("ID:", emp_id)
print("Name:", emp_name)
print("Salary:", salary)

# Nested Tuple
projects = (
    ("Project A", "Completed"),
    ("Project B", "In Progress")
)

print("\nProjects:")
for project_name, status in projects:
    print(project_name, "-", status)

