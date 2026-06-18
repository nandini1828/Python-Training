# String methods
message = "  python is easy  "
print("Original:", message)
print("After strip:", message.strip())
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Replace:", message.replace("easy", "fun"))

# List methods
items = ["pen", "book", "pencil"]
items.append("eraser")
items.insert(1, "notebook")
print("After adding:", items)
print("Removed item:", items.pop())
print("Current list:", items)

# Dictionary methods
student = {
    "name": "Meena",
    "age": 20,
    "city": "Delhi"
}
print("Keys:", student.keys())
print("Values:", student.values())
print("Name:", student.get("name"))
student["age"] = 21
print("Updated student:", student)

# Set methods
colors = {"red", "blue", "green"}
colors.add("yellow")
colors.remove("blue")
print("Colors:", colors)

# Tuple methods
marks = (80, 90, 80, 85)
print("Count of 80:", marks.count(80))
print("Index of 85:", marks.index(85))
