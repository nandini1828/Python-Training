# Creating a dictionary
employee = {
    "id": 101,
    "name": "Karthik",
    "salary": 50000
}
print("\nOriginal Dictionary")
print(employee)

# get()
print("\nget()")
print( employee.get("name"))
print(employee.get("city", "Not Found"))

# setdefault()
print("\nsetdefault()")
employee.setdefault("department","IT")
print(employee)

# keys()
print("\nkeys()")
print(employee.keys())

# values()
print("\nvalues()")
print(employee.values())

# items()
print("\nitems()")
print(employee.items())

# update()
print("\nupdate()")
employee.update(
    {
        "salary": 60000
    }
)
print(employee)

# pop()
print("\npop()")
removed_salary = employee.pop("salary")
print(f"Removed Salary: {removed_salary}")
print(employee)

# copy()
print("\ncopy()")
employee_copy = employee.copy()
print(employee_copy)

# fromkeys()
print("\nfromkeys()")
students = dict.fromkeys(
    ["student1", "student2", "student3"],
    "Present"
)
print(students)

# clear()
print("\nclear()")
temp_data = {
    "a": 1,
    "b": 2
}
temp_data.clear()
print(temp_data)

# Do Python developers directly use dunder methods like __add__() and __eq__(), 
# or are they mainly used internally by Python?
# Regarding pytest, where it is used in real time
# About serialization and deserialization
# The primary purpose of pytest is to simplify and automate the process of writing, discovering, and executing test cases in Python
# Where to use isinstance() and where to use type()
