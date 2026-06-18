class Student:
    def __init__(self, name, age, grade):
        # Instance variables (unique to each object)
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def is_pass(self):
        return self.grade >= 40


# Creating objects (instances of the class)
student1 = Student("Vishnu", 21, 85)
student2 = Student("Laxmi", 20, 35)

# Accessing object attributes
print(student1.name)
print(student1.age)
print(student1.grade)

# Calling methods
print(student1.info())
print(student1.is_pass())

print(student2.info())
print(student2.is_pass())
