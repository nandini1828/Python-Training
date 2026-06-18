#LIST:
#A List is an ordered collection of items.

from tokenize import String


fruits = ["Apple", "Banana", "Mango"]
print(fruits)

# Access elements using index
print(fruits[0])  # Apple
print(fruits[1])  # Banana

# Add new item
fruits.append("Orange")
print(fruits)

# Remove item
fruits.remove("Banana")
print(fruits)

# Change item
fruits[0] = "Grapes"
print(fruits)

# Length of list
print(len(fruits))

# Loop through list
for fruit in fruits:
    print(fruit)

"""
Real Life Example:

Shopping List:
["Milk", "Bread", "Eggs"]

School Students:
["John", "David", "Emma"]
"""
#-------------#-------------#--------------#-------------#------------#-------------#------------#------------#

#TUPLE:
#A Tuple is similar to a list but cannot be changed after creation.

colors = ("Red", "Green", "Blue")

print(colors)

# Access elements
print(colors[0])

# Length
print(len(colors))

"""
Tuples are Immutable

This will cause an error:

colors[0] = "Yellow"

Why?

Because tuples cannot be modified.
"""

"""
Real Life Example:

Days of Weekend:
("Saturday", "Sunday")

Coordinates:
(17.3850, 78.4867)
"""
#-------------#-------------#--------------#-------------#------------#-------------#------------#------------#
#SET
#A Set stores unique values only.

numbers = {1, 2, 3, 4, 4, 5, 5}

print(numbers)

"""
Output:
{1, 2, 3, 4, 5}

Duplicate values are automatically removed.
"""

# Add value
numbers.add(6)

# Remove value
numbers.remove(2)
print(numbers)

# Check existence
print(3 in numbers)

"""
Real Life Example:

Unique Student IDs

{101, 102, 103}

No duplicates allowed.
"""
#-------------#-------------#--------------#-------------#------------#-------------#------------#------------#

# DICTIONARY:
#Stores data as Key : Value pairs.
student = {
    "name": "John",
    "age": 15,
    "grade": "10th"
}

print(student)

# Access values
print(student["name"])
print(student["age"])

# Add new key-value pair
student["city"] = "Hyderabad"

# Update value
student["age"] = 16

print(student)

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)

"""
Real Life Example:

Student Record

{
    "name": "Sagar",
    "age": 20,
    "college": "XYZ"
}
"""
#-------------#-------------#--------------#-------------#------------#-------------#------------#------------#
#STRING:
#A String is a collection of characters.

name = "Python"
print(name)

# First character
print(name[0])

# Last character
print(name[-1])

# Length
print(len(name))

# Loop through string
for char in name:
    print(char)

"""
Real Life Example:

Student Name
Book Title
Email Address

All are Strings.
"""
#-------------#-------------#--------------#-------------#------------#-------------#------------#------------#

#STACK
#Last In First Out
#Example: Stack of Plates

stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# Pop element
removed = stack.pop()

print("Removed:", removed)
print(stack)

"""
Stack Visualization

Top
30 <- Removed First
20
10

Bottom

LIFO = Last In First Out
"""

#-------------#-------------#--------------#-------------#------------#-------------#------------#------------#
#Queue (FIFO)
#First In First Out
#Example: Ticket Counter Queue

from collections import deque

queue = deque()

# Add people
queue.append("John")
queue.append("David")
queue.append("Emma")

print(queue)

# Remove first person
print(queue.popleft())

print(queue)

"""
Queue Visualization

John  -> Served First
David
Emma

FIFO = First In First Out
"""