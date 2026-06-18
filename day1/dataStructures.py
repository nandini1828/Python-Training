""" A Data Structure is a way of storing and organizing data so that it can be used efficiently."""

# Common Data Structures in Python

# 1. List
employees = ["Karthik", "Rahul", "koushik"]

employees.append("Anil")  # Adds "Anil" to the end of the list
print(employees)  # Output: ['Karthik', 'Rahul', 'koushik', 'Anil']
employees.remove("Rahul")  # Removes "Rahul" from the list
print(employees)  # Output: ['Karthik', 'koushik', 'Anil']

# 2. Tuple
location = (17.3850, 78.4867)
# Use when:
""" Data is fixed
 Read-only values"""


# 3. Dictionary
employee = {
    "name": "Karthik",
    "age": 21,
    "department": "IT"
}
print(employee["name"])  # Output: "Karthik"
print(employee["age"])  # Output: 21
print(employee["department"])  # Output: "IT"


# 4. Set
skills = {"Java", "Python", "C++"}
print(skills)  # Output: {'Java', 'Python', 'C++'}
# Use when:
""" Unique values
 Unordered collection
 No duplicates allowed"""


# 5. Stack (LIFO)
stack = []
stack.append(1)  # Push 1 onto the stack
stack.append(2)  # Push 2 onto the stack
print(stack)  # Output: [1, 2]
stack.pop()  # Pop the top element (2) from the stack
print(stack)  # Output: [1]

# 6. Queue (FIFO)
queue = []
queue.append(1)  # Enqueue 1
queue.append(2)  # Enqueue 2
print(queue)  # Output: [1, 2]
queue.pop(0)  # Dequeue the front element (1) from the queue
print(queue)  # Output: [2]


# Linked List
"""Nodes connected using pointers."""
linked_list = {
    "value": 1,
    "next": {
        "value": 2,
        "next": {
            "value": 3,
            "next": None
        }
    }
}
# Used in navigation systems


# Tree
"""Hierarchical structure."""


# Graph
"""Nodes connected by edges."""