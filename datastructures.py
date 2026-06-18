# 1. List - stores items in order
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print("Fruits:", fruits)

# 2. Tuple - stores items that should not change easily
point = (10, 20)
print("Point:", point)

# 3. Dictionary - stores data as key-value pairs
student = {
    "name": "Vishnu",
    "age": 21,
    "course": "Python"
}
print("Student info:", student)
print("Student name:", student["name"])

# 4. Set - stores unique values
numbers = {1, 2, 2, 3}
print("Unique numbers:", numbers)

# 5. Stack (LIFO) - last item added is removed first
stack = []
stack.append("book")
stack.append("pen")
stack.append("notebook")
print("Stack before pop:", stack)
print("Removed item:", stack.pop())
print("Stack after pop:", stack)

# 6. Queue (FIFO) - first item added is removed first
queue = []
queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")
print("Queue before removing:", queue)
print("Removed item:", queue.pop(0))
print("Queue after removing:", queue)

