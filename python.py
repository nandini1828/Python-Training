from abc import ABC, abstractmethod

class Character(ABC):

@abstractmethod
def role(self):
    pass

class IndianaJones(Character):

def __init__(self, name, health):
    self.__name = name
    self.__health = health

def get_name(self):
    return self.__name

def get_health(self):
    return self.__health

def set_health(self, health):
    self.__health = health

def role(self):
    return "Treasure Explorer"

def show(self):
    return f"{self.__name} | Health: {self.__health}"

missions = ["Temple Run", "Golden Cave", "Ice Fortress"]

coordinates = (12.5, 77.2)

inventory = {"whip", "hat", "torch"}

mission_status = {"Temple Run": "Completed","Golden Cave": "Ongoing"}

class Enemy(Character):

def role(self):
    return "Guardian of Treasure"

name = "indiana jones"

upper_name = name.upper()title_name = name.title()

missions.append("Desert Temple")

inventory.add("map")

mission_status["Desert Temple"] = "Locked"

def main():

indy = IndianaJones("Indiana Jones", 100)

enemy = Enemy()

print("\n--- OOP SECTION ---")
print(indy.show())
print("Role:", indy.role())
print("Enemy Role:", enemy.role())

print("\n--- DATA TYPE METHODS ---")
print("Upper:", upper_name)
print("Title:", title_name)

print("\n--- DATA STRUCTURES ---")
print("Missions:", missions)
print("Coordinates:", coordinates)
print("Inventory:", inventory)
print("Mission Status:", mission_status)

indy.set_health(80)

print("\nUpdated Health:", indy.get_health())

if name == "main":main()