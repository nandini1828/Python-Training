# =========================
# STRING METHODS
# =========================

text = "   python programming   "

print(text.strip())          # Remove spaces
print(text.upper())          # Uppercase
print(text.lower())          # Lowercase
print(text.capitalize())     # First letter capital
print(text.replace("python", "java"))
print(text.split())          # String -> List
print(len(text))

# =========================
# LIST METHODS
# =========================

numbers = [10, 20, 30]

numbers.append(40)
numbers.insert(1, 15)
numbers.remove(20)
numbers.sort()
numbers.reverse()

print(numbers)
print(len(numbers))
print(numbers.count(30))
print(numbers.index(15))

# =========================
# TUPLE METHODS
# =========================

data = (1, 2, 3, 2, 4, 2)

print(data.count(2))
print(data.index(3))

# =========================
# SET METHODS
# =========================

skills = {"Python", "Java"}

skills.add("SQL")
skills.remove("Java")

backend = {"Python", "SQL"}
frontend = {"React", "JavaScript"}

print(skills)
print(backend.union(frontend))
print(backend.intersection({"Python", "FastAPI"}))

# =========================
# DICTIONARY METHODS
# =========================

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

# =========================
# TYPE CONVERSIONS
# =========================

num = "100"

print(int(num))
print(float(num))
print(str(100))
print(list("Python"))
print(tuple([1, 2, 3]))
print(set([1, 1, 2, 3]))

# =========================
# BOOLEAN METHODS
# =========================

print(bool(1))
print(bool(0))
print(bool("Hello"))
print(bool(""))

# =========================
# CHECKING METHODS
# =========================

print("Python".isalpha())
print("123".isdigit())
print("Python123".isalnum())
print("python".islower())
print("PYTHON".isupper())