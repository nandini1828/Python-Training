"""
Class Manager

Unified interface for managing all class examples.
"""

from typing import Dict, List, Any
from .student import Student
from .employee import Employee
from .department import Department
from .composition import Company, Address, Office


class ClassManager:
    """Manager for class examples and demonstrations."""
    
    def __init__(self):
        """Initialize the class manager."""
        self.students: List[Student] = []
        self.employees: List[Employee] = []
        self.departments: List[Department] = []
        self.companies: List[Company] = []
    
    def create_student(self, student_id: str, name: str, major: str, 
                      gpa: float = 0.0) -> Student:
        """
        Create a new student.
        
        Args:
            student_id: Student ID.
            name: Student name.
            major: Major field.
            gpa: Initial GPA.
            
        Returns:
            Student: Created student instance.
        """
        student = Student(student_id, name, major, gpa)
        self.students.append(student)
        return student
    
    def create_employee(self, employee_id: str, name: str, position: str,
                       salary: float, department: str = "General") -> Employee:
        """
        Create a new employee.
        
        Args:
            employee_id: Employee ID.
            name: Employee name.
            position: Job position.
            salary: Annual salary.
            department: Department name.
            
        Returns:
            Employee: Created employee instance.
        """
        employee = Employee(employee_id, name, position, salary, department)
        self.employees.append(employee)
        return employee
    
    def create_department(self, name: str, manager_id: str,
                         budget: float = 100000.0) -> Department:
        """
        Create a new department.
        
        Args:
            name: Department name.
            manager_id: Manager employee ID.
            budget: Department budget.
            
        Returns:
            Department: Created department instance.
        """
        dept = Department(name, manager_id, budget)
        self.departments.append(dept)
        return dept
    
    def create_company(self, name: str, address: Address) -> Company:
        """
        Create a new company.
        
        Args:
            name: Company name.
            address: Headquarters address.
            
        Returns:
            Company: Created company instance.
        """
        company = Company(name, address)
        self.companies.append(company)
        return company
    
    def get_demo_data(self) -> Dict[str, Any]:
        """
        Get sample data demonstrating all class features.
        
        Returns:
            Dict[str, Any]: Sample data.
        """
        # Create sample students
        student1 = self.create_student("S001", "Alice Johnson", "Computer Science", 3.8)
        student1.enroll_course("Python Basics")
        student1.enroll_course("Data Structures")
        
        student2 = self.create_student("S002", "Bob Smith", "Information Technology", 3.2)
        student2.enroll_course("Web Development")
        
        # Create sample employees
        emp1 = self.create_employee("E001", "Carol White", "Senior Developer", 120000)
        emp1.add_performance_review(95, "Excellent performer")
        
        emp2 = self.create_employee("E002", "David Brown", "Junior Developer", 60000)
        emp2.add_performance_review(85, "Good progress")
        
        # Create department with employees
        dept = self.create_department("Engineering", "E001", 500000)
        dept.add_employee(emp1)
        dept.add_employee(emp2)
        
        # Create company with offices
        hq_address = Address("123 Tech St", "San Francisco", "CA", "94105")
        company = self.create_company("TechCorp", hq_address)
        
        office_address = Address("456 Code Ave", "New York", "NY", "10001")
        ny_office = Office("NY01", office_address, 3, 200)
        company.add_office(ny_office)
        
        return {
            "students": [s.get_info() for s in self.students],
            "employees": [e.get_info() for e in self.employees],
            "departments": [d.get_department_info() for d in self.departments],
            "companies": [c.get_company_info() for c in self.companies],
        }
    
    def get_summary(self) -> Dict[str, int]:
        """
        Get summary of managed objects.
        
        Returns:
            Dict[str, int]: Count of each type.
        """
        return {
            "total_students": len(self.students),
            "total_employees": len(self.employees),
            "total_departments": len(self.departments),
            "total_companies": len(self.companies),
        }
