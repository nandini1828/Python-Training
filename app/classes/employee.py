"""
Employee Class

Demonstrates class with additional attributes and methods for employees.
"""

from typing import Dict, Optional
from datetime import datetime, timedelta


class Employee:
    """
    Represents an employee with employment information.
    
    Attributes:
        employee_id: Unique employee identifier.
        name: Employee full name.
        department: Department name.
        position: Job position/title.
        salary: Annual salary.
        hire_date: Date of employment.
        is_active: Employment status.
    """
    
    # Class variables
    company_name = "Tech Corp"
    min_salary = 20000.0
    total_employees = 0
    
    def __init__(self, employee_id: str, name: str, position: str,
                 salary: float, department: str = "General"):
        """
        Initialize an Employee instance.
        
        Args:
            employee_id: Unique identifier.
            name: Full name.
            position: Job title.
            salary: Annual salary.
            department: Department name.
            
        Raises:
            ValueError: If salary is below minimum.
        """
        if salary < Employee.min_salary:
            raise ValueError(f"Salary must be >= {Employee.min_salary}")
        
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
        self.department = department
        self.hire_date = datetime.now()
        self.is_active = True
        self.reviews: list = []
        
        Employee.total_employees += 1
    
    def give_raise(self, percentage: float) -> float:
        """
        Give employee a raise by percentage.
        
        Args:
            percentage: Percentage increase.
            
        Returns:
            float: New salary.
            
        Raises:
            ValueError: If percentage is invalid.
        """
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
        
        increase = self.salary * (percentage / 100)
        self.salary += increase
        return self.salary
    
    def add_performance_review(self, score: float, comments: str = "") -> None:
        """
        Add a performance review.
        
        Args:
            score: Review score (0-100).
            comments: Review comments.
            
        Raises:
            ValueError: If score is invalid.
        """
        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100")
        
        review = {
            "date": datetime.now(),
            "score": score,
            "comments": comments,
        }
        self.reviews.append(review)
    
    def get_average_review_score(self) -> Optional[float]:
        """
        Get average performance review score.
        
        Returns:
            Optional[float]: Average score or None if no reviews.
        """
        if not self.reviews:
            return None
        
        total = sum(review["score"] for review in self.reviews)
        return total / len(self.reviews)
    
    def promote(self, new_position: str, salary_increase: float) -> None:
        """
        Promote employee to new position.
        
        Args:
            new_position: New job title.
            salary_increase: Salary increase amount.
            
        Raises:
            ValueError: If salary increase is negative.
        """
        if salary_increase < 0:
            raise ValueError("Salary increase must be non-negative")
        
        self.position = new_position
        self.salary += salary_increase
    
    def calculate_years_employed(self) -> float:
        """
        Calculate years of employment.
        
        Returns:
            float: Years employed.
        """
        delta = datetime.now() - self.hire_date
        return delta.days / 365.25
    
    def get_employment_status(self) -> Dict[str, object]:
        """
        Get current employment status.
        
        Returns:
            Dict[str, object]: Employment status information.
        """
        return {
            "is_active": self.is_active,
            "years_employed": round(self.calculate_years_employed(), 2),
            "salary": self.salary,
            "reviews_count": len(self.reviews),
            "average_score": round(self.get_average_review_score(), 2) 
                           if self.reviews else None,
        }
    
    def get_info(self) -> Dict[str, object]:
        """
        Get complete employee information.
        
        Returns:
            Dict[str, object]: All employee details.
        """
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "position": self.position,
            "department": self.department,
            "salary": self.salary,
            "hire_date": self.hire_date,
            "is_active": self.is_active,
            "reviews": len(self.reviews),
            "avg_review": self.get_average_review_score(),
        }
    
    def terminate_employment(self) -> None:
        """Terminate employee's employment."""
        self.is_active = False
    
    def __str__(self) -> str:
        """String representation."""
        return f"Employee({self.employee_id}, {self.name}, {self.position})"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (f"Employee(employee_id='{self.employee_id}', name='{self.name}', "
                f"position='{self.position}', salary={self.salary})")
    
    @classmethod
    def get_total_employees(cls) -> int:
        """Get total employees created."""
        return cls.total_employees
    
    @classmethod
    def set_minimum_salary(cls, salary: float) -> None:
        """Set minimum salary requirement."""
        cls.min_salary = salary
    
    @staticmethod
    def is_valid_position(position: str) -> bool:
        """Check if position is valid."""
        valid_positions = {
            "Intern", "Junior", "Senior", "Lead", "Manager", "Director", "VP", "CEO"
        }
        return position in valid_positions
