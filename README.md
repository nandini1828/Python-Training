# Indiana Jones OOP Program - Full Explanation


 1. Introduction

This program simulates a small **Indiana Jones adventure system** using:

- Object-Oriented Programming (OOP)
- Data Structures
- String Methods
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction


2. Abstraction

python
from abc import ABC, abstractmethod
📖 Meaning

Abstraction hides implementation details and shows only required behavior.

 Why used here?

We force all characters to define a role() method.

Abstract Class
class Character(ABC):
Explanation
Character is a blueprint
Cannot be directly used
Used for inheritance
Abstract Method
@abstractmethod
def role(self):
    pass
Meaning

Every character MUST define their role.

3. Inheritance (Indiana Jones Class)
class IndianaJones(Character):
Explanation
IndianaJones inherits from Character
Gets structure from parent class
Constructor
def __init__(self, name, health):
    self.__name = name
    self.__health = health
Meaning
Initializes player data
__name and __health are PRIVATE (Encapsulation)

 4. Encapsulation
Private Variables
self.__name
self.__health
Meaning
Cannot be accessed directly
Must use getter/setter methods
Getter Methods
def get_name(self):
    return self.__name

def get_health(self):
    return self.__health
Purpose

Safely access private data.

Setter Method
def set_health(self, health):
    self.__health = health
Purpose

Safely update health value.

 5. Polymorphism
def role(self):
    return "Treasure Explorer"
Meaning

Same method (role) behaves differently in different classes.

Enemy Class
class Enemy(Character):
    def role(self):
        return "Guardian of Treasure"
Output Difference
Indiana → Treasure Explorer
Enemy → Guardian of Treasure

 6. Data Structures
📌 List
missions = ["Temple Run", "Golden Cave", "Ice Fortress"]
Meaning

Stores multiple missions.

📌 Tuple
coordinates = (12.5, 77.2)
Meaning

Fixed treasure location (cannot change).

📌 Set
inventory = {"whip", "hat", "torch"}
Meaning

Unique items only (no duplicates).

📌 Dictionary
mission_status = {
    "Temple Run": "Completed",
    "Golden Cave": "Ongoing"
}
Meaning

Stores mission → status mapping.

7. String Methods
name = "indiana jones"
Methods
upper_name = name.upper()
title_name = name.title()
Output Meaning
uppercase version
properly formatted name

8. Data Updates
missions.append("Desert Temple")
inventory.add("map")
mission_status["Desert Temple"] = "Locked"
Meaning
Add new mission
Add new inventory item
Add new mission status

9. Main Function
def main():
Meaning

Starting point of the program.

10. Object Creation
indy = IndianaJones("Indiana Jones", 100)
enemy = Enemy()
Meaning
Creates player object
Creates enemy object

11. Output Section
print(indy.show())
print(indy.role())
print(enemy.role())
Output Explanation
show() → shows player details
role() → shows Indiana role
enemy role → shows enemy role

12. Health Update
indy.set_health(80)
Meaning

Indiana got injured → health reduced

print(indy.get_health())
Output
80

13. FINAL OUTPUT
--- OOP SECTION ---
Indiana Jones | Health: 100
Role: Treasure Explorer
Enemy Role: Guardian of Treasure

--- DATA TYPE METHODS ---
Upper: INDIANA JONES
Title: Indiana Jones

--- DATA STRUCTURES ---
Missions: ['Temple Run', 'Golden Cave', 'Ice Fortress', 'Desert Temple']
Coordinates: (12.5, 77.2)
Inventory: {'whip', 'hat', 'torch', 'map'}
Mission Status: {'Temple Run': 'Completed', 'Golden Cave': 'Ongoing', 'Desert Temple': 'Locked'}

Updated Health: 80
