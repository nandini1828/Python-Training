# INTROSPECTION TOOLS 

# type()
# dir()
# id()
# list_public_attributes()

name = "Karthik"

print(type(name))  
# Type returns the type of the variable. In this case, it will return <class 'str'> since name is a string.
print(dir(name))
# Dir returns a list of all the attributes and methods associated with the variable. In this case, it will return a list of all the methods and attributes that can be used with a string object.
print(id(name)) 
# Id returns the unique identifier for the variable. In this case, it will return a unique integer that represents the memory address of the variable name.

age = 21
print(type(age))
# output:
# <class 'str'>

print(id(age))
# Output:
# 140711234567456 (This will vary each time you run the code)


"""
This file demonstrates Python introspection concepts:

1. type()
2. id()
3. dir()
4. Public attribute extraction

Introspection means inspecting objects at runtime.
"""
def list_public_attributes(obj):
    """
    Returns only public attributes and methods.
    Parameters:
        obj: Any Python object
    Returns:
        list: Public attributes/method names
    """
    return[
        attribute_name
        for attribute_name in dir(obj)
        if not attribute_name.startswith("_")
    ]
def display_object_information(obj):
    """
    Displays basic information about any object.
    Parameters:
        obj: Any Python object
    """
    print("\nObject Information")
    print("-" * 30)
    print(f"Value : {obj}")
    print(f"Type  : {type(obj)}")
    print(f"ID    : {id(obj)}")

if __name__ == "__main__":
    # Example 1
    employee_name = "Karthik"
    display_object_information(employee_name)
    print("\nPublic Methods:")
    print(list_public_attributes(employee_name))
    # Example 2
    employee_salary = 50000
    display_object_information(employee_salary)
    print("\nPublic Methods:")
    print(list_public_attributes(employee_salary))