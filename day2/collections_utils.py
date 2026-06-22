# LIST
skills = ["Python", "FastAPI"]
skills.append("AWS")      # Add item
skills.insert(1, "SQL")   # Add at specific position
print("List:", skills)

# TUPLE
numbers = (1, 2, 2, 3)
print("Count of 2:", numbers.count(2))
print("Index of 3:", numbers.index(3))
# Typle methods 
# SET
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# QUEUE
queue = []

queue.append("Python")   # Enqueue
queue.append("FastAPI")
print("Queue:", queue)
item = queue.pop(0)      # Dequeue
print("Removed:", item)
print("Queue after dequeue:", queue)

# TAG MERGING USING SETS
tags1 = {"python", "java"}
tags2 = {"python", "aws"}
print("All Tags:", tags1 | tags2)
print("Common Tags:", tags1 & tags2)