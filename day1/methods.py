# * A data type = a thing (string, list, dictionary, etc.)
# * A method = an action that thing can perform

# String Methods
name = "karthik"
print(name.upper())  # Output: "KARTHIK"
print(name.lower())  # Output: "karthik"
print(name.title())  # Output: "Karthik"        
print(name.strip())  # Output: "karthik" (removes leading/trailing whitespace)
print(name.replace("k", "c"))  # Output: "carthic" (replaces 'k' with 'c')
print(name.split("r"))  # Output: ['ka', 'thik'] (splits the string at 'r')
print(name.find("t"))  # Output: 3 (finds the index of 't')
print(name.startswith("k"))  # Output: True (checks if the string starts with 'k')
print(name.endswith("k"))  # Output: True (checks if the string ends with 'k)


# List Methods
employees = ["Karthik", "koushik" , "Rajesh", "Suresh"]
print(employees.append("Ramesh"))  # Output: None (adds "Ramesh" to the end of the list)
print(employees.insert(1, "Anil"))  # Output: None (inserts "Anil" at index 1)
print(employees.remove("Rajesh"))  # Output: None (removes "Rajesh" from the list)
print(employees.pop())  # Output: "Ramesh" (removes and returns the last item)
print(employees.sort())  # Output: None (sorts the list in place)
print(employees.reverse())  # Output: None (reverses the list in place)
print(employees.index("Suresh"))  # Output: 2 (finds the index of "Suresh")
print(employees.count("Karthik"))  # Output: 1 (counts the occurrences of "Karthik")
print(employees.clear())  # Output: None (removes all items from the list)


# Dictionary Methods
student = {
    "name":"karthik","age":21,
    "course":"Btech",
    "grade":"A"
}
print(student.keys())  # Output: dict_keys(['name', 'age', 'course', 'grade']) (returns a view of the dictionary's keys)
print(student.values())  # Output: dict_values(['karthik', 21, 'Btech', 'A']) (returns a view of the dictionary's values)
print(student.items())  # Output: dict_items([('name', 'karthik'), ('age', 21), ('course', 'Btech'), ('grade', 'A')]) (returns a view of the dictionary's key-value pairs)
print(student.get("name"))  # Output: "karthik" (returns the value associated with the key "name")
print(student.update({"grade": "A+"}))  # Output: None (updates the value of "grade" to "A+")
print(student.pop("age"))  # Output: 21 (removes and returns the value associated with the key "age")
print(student.clear())  # Output: None (removes all items from the dictionary)


# Set Methods
skills = {"Java","Python","C++"}
print(skills.add("JavaScript"))  # Output: None (adds "JavaScript" to the set)
print(skills.remove("C++"))  # Output: None (removes "C++" from the set)
print(skills.discard("Ruby"))  # Output: None (removes "Ruby" from the set if it exists, does nothing if it doesn't)
print(skills.clear())  # Output: None (removes all items from the set)


# Tuple Methods
marks = (85, 90, 78, 92)
print(marks.count(90))  # Output: 1 (counts the occurrences of 90 in the tuple)
print(marks.index(78))  # Output: 2 (finds the index of 78 in the tuple)


