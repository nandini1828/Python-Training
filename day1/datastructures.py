# ==================================
# LIST
# ==================================

numbers = [10, 20, 30]

numbers.append(40)
numbers.insert(1, 15)
numbers.remove(20)
numbers.pop()
numbers.extend([50, 60])
numbers.sort()

print("List:", numbers)

# ==================================
# TUPLE
# ==================================

data = (10, 20, 30, 20, 40)

print("Count:", data.count(20))
print("Index:", data.index(30))

# ==================================
# SET
# ==================================

skills = {"Python", "Java"}

skills.add("SQL")
skills.update(["FastAPI", "Flask"])
skills.remove("Java")

backend = {"Python", "SQL", "FastAPI"}

print("Union:", skills.union(backend))
print("Intersection:", skills.intersection(backend))
print("Difference:", skills.difference(backend))

# ==================================
# DICTIONARY
# ==================================

student = {
    "name": "Bhavya",
    "age": 21
}

student["city"] = "Hyderabad"

print(student.get("name"))
print(student.keys())
print(student.values())
print(student.items())

student.update({"age": 22})
student.pop("city")

print(student)

# ==================================
# STRING (VERY IMPORTANT)
# ==================================

text = " python programming "

print(text.strip())
print(text.upper())
print(text.lower())
print(text.replace("python", "java"))
print(text.split())

# ==================================
# PRACTICE WITH ALL DATA STRUCTURES
# ==================================

fruits = ["Apple", "Banana", "Apple", "Orange"]

# Convert List -> Set
unique_fruits = set(fruits)

# Convert Set -> List
fruit_list = list(unique_fruits)

# Convert List -> Tuple
fruit_tuple = tuple(fruit_list)

# Create Dictionary
fruit_dict = {
    "Apple": 100,
    "Banana": 50,
    "Orange": 80
}

print(unique_fruits)
print(fruit_list)
print(fruit_tuple)
print(fruit_dict)