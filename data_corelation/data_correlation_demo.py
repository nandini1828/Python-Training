import json

# Python representation of data
employee = {
    "id": 101,
    "name": "Karthik",
    "skills": ["Python", "SQL"],
    "address": {
        "city": "Hyderabad",
        "pincode": 500001
    },
    "active": True
}

print("Original Python dictionary:")
print(employee)
print()

# Convert Python dict to JSON
employee_json = json.dumps(employee, indent=4)
print("Converted to JSON:")
print(employee_json)
print()

# Simulate frontend/JS receiving same structure
frontend_payload = json.loads(employee_json)
print("Frontend-like payload converted back to Python:")
print(frontend_payload)
print()

# Simulate NoSQL document (same structure as dict/JSON)
nosql_document = employee.copy()
nosql_document["department"] = "Engineering"
print("NoSQL-style document:")
print(nosql_document)
print()

# Simulate RDBMS style data
employee_row = {
    "id": 101,
    "name": "Karthik",
    "active": True
}

employee_skills_rows = [
    {"employee_id": 101, "skill": "Python"},
    {"employee_id": 101, "skill": "SQL"}
]

print("RDBMS employee row:")
print(employee_row)
print()

print("RDBMS employee skills rows:")
print(employee_skills_rows)
print()

# Dictionary and list operations
employee["skills"].append("Java")
employee["address"]["city"] = "Bangalore"
employee["email"] = "karthik@example.com"

print("After updates in Python dict/list:")
print(employee)
print()

# Remove a skill
employee["skills"].remove("SQL")
print("After removing SQL:")
print(employee)
print()