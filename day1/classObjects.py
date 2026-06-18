# Class -> blueprint/template for creating objects
# Object -> instance of a class (real thing that is created using blueprint)

# Example of class
class Student:
    pass

# Object = instance of a class
# Example of creating an object
student1 = Student() 
student2 = Student()
# here student1 and student2 are objects of the Student class


# COMPLETE EXAMPLE
class Student:
    
    def __init__(self,name,marks,grade):
        self.name = name
        self.marks = marks
        self.grade = grade

student1 = Student("Karthik",85,"A")
print(student1.name)  # Output: "Karthik"
print(student1.marks)  # Output: 85
print(student1.grade)  # Output: "A"

# SELF -> # Creates an instance variable unique to the object


# Real World           OOP

# Building plan       Class

# Actual building     Object

# Vehicle design      Class

# Honda City car      Object

# Employee format      Class

# Karthik employee     Object
# record
