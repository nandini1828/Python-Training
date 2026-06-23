# List
students = ["Nandini", "Rahul", "Priya"]
print(students)
print(students[0])
students.append("Kiran")
print(students)

# Tuple
student = ("Nandini", 20, "CSE")
print(student)
print(student[0])
print(student[1])

# Set
numbers = {1, 2, 3, 4, 4, 5}
print(numbers)
numbers.add(6)
print(numbers)

# Dictionary
student = {
    "name": "Nandini",
    "age": 20,
    "branch": "CSE"
}
print(student)
print(student["name"])
print(student["age"])

# Stack using List
stack = []
stack.append("Book 1")
stack.append("Book 2")
stack.append("Book 3")
print(stack)
stack.pop()
print(stack)

# Queue using List
queue = []
queue.append("Person 1")
queue.append("Person 2")
queue.append("Person 3")
print(queue)
queue.pop(0)
print(queue)

# Nested List
students = [
    ["Nandini", 20],
    ["Rahul", 21],
    ["Priya", 22]
]
print(students)
print(students[0])
print(students[0][0])

# List Traversal
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)

# Tuple Traversal
numbers = (10, 20, 30, 40)
for number in numbers:
    print(number)

# Set Traversal
numbers = {10, 20, 30, 40}
for number in numbers:
    print(number)

# Dictionary Traversal
student = {
    "name": "Nandini",
    "age": 20,
    "branch": "CSE"
}
for key, value in student.items():
    print(key, value)

# List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = [num * num for num in numbers]
print(squares)

# Dictionary Comprehension
squares = {num: num * num for num in range(1, 6)}
print(squares)