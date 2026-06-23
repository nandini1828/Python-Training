from abc import ABC, abstractmethod



class Person(ABC):

    @abstractmethod
    def display_info(self):
        pass


# Inheritance
class Employee(Person):

    def __init__(self, emp_id, name, salary):
        # Encapsulation
        self.__emp_id = emp_id
        self.name = name.title()      # String Method
        self.salary = float(salary)

        # Data Structures
        self.skills = []             # List
        self.projects = set()        # Set
        self.details = {}            # Dictionary

    def add_skills(self, *skills):
        self.skills.extend(skills)


    def add_projects(self, *projects):
        self.projects.update(projects)

    def update_details(self, **kwargs):
        self.details.update(kwargs)

  
    def display_info(self):

        print("\nEmployee Information")
        print("--------------------")

        print(f"Employee ID : {self.__emp_id}")
        print(f"Name        : {self.name}")
        print(f"Salary      : {self.salary}")

        print("\nSkills:")
        for skill in self.skills:
            print(skill)

        print("\nProjects:")
        for project in self.projects:
            print(project)

        print("\nAdditional Details:")
        for key, value in self.details.items():
            print(f"{key} : {value}")

        print("\nData Types")
        print(type(self.__emp_id))
        print(type(self.name))
        print(type(self.salary))
        print(type(self.skills))
        print(type(self.projects))
        print(type(self.details))



employee = Employee(
    101,
    "vyshnavi",
    50000
)


employee.add_skills(
    "Python",
    "FastAPI",
    "Git"
)

# Set Methods
employee.add_projects(
    "CRM",
    "Insurance Portal",
    "CRM"  
)


employee.update_details(
    age=22,
    city="Hyderabad",
    experience="Fresher"
)

employee.display_info()