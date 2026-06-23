"""
Department Class

Demonstrates managing collections of employees.
"""

from typing import List, Dict, Optional
from .employee import Employee


class Department:
    """
    Represents a company department managing employees.
    
    Attributes:
        name: Department name.
        manager_id: ID of department manager.
        employees: List of employees in department.
        budget: Department budget.
    """
    
    def __init__(self, name: str, manager_id: str, budget: float = 100000.0):
        """
        Initialize a Department.
        
        Args:
            name: Department name.
            manager_id: Manager employee ID.
            budget: Department budget.
        """
        self.name = name
        self.manager_id = manager_id
        self.budget = budget
        self.employees: List[Employee] = []
        self.creation_date = datetime.now()
    
    def add_employee(self, employee: Employee) -> bool:
        """
        Add employee to department.
        
        Args:
            employee: Employee to add.
            
        Returns:
            bool: True if added, False if already in department.
        """
        if employee not in self.employees:
            self.employees.append(employee)
            employee.department = self.name
            return True
        return False
    
    def remove_employee(self, employee_id: str) -> Optional[Employee]:
        """
        Remove employee from department.
        
        Args:
            employee_id: ID of employee to remove.
            
        Returns:
            Optional[Employee]: Removed employee or None.
        """
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                return employee
        return None
    
    def get_employee(self, employee_id: str) -> Optional[Employee]:
        """
        Find employee by ID.
        
        Args:
            employee_id: Employee ID.
            
        Returns:
            Optional[Employee]: Found employee or None.
        """
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None
    
    def get_payroll(self) -> float:
        """
        Calculate total payroll for department.
        
        Returns:
            float: Total salary expenses.
        """
        return sum(emp.salary for emp in self.employees)
    
    def get_average_salary(self) -> Optional[float]:
        """
        Calculate average salary.
        
        Returns:
            Optional[float]: Average salary or None if no employees.
        """
        if not self.employees:
            return None
        return self.get_payroll() / len(self.employees)
    
    def get_budget_remaining(self) -> float:
        """
        Get remaining budget after payroll.
        
        Returns:
            float: Remaining budget.
        """
        return self.budget - self.get_payroll()
    
    def is_over_budget(self) -> bool:
        """
        Check if department is over budget.
        
        Returns:
            bool: True if over budget.
        """
        return self.get_payroll() > self.budget
    
    def get_department_info(self) -> Dict[str, object]:
        """
        Get complete department information.
        
        Returns:
            Dict[str, object]: Department details.
        """
        return {
            "name": self.name,
            "manager_id": self.manager_id,
            "employee_count": len(self.employees),
            "total_payroll": self.get_payroll(),
            "average_salary": self.get_average_salary(),
            "budget": self.budget,
            "remaining_budget": self.get_budget_remaining(),
            "is_over_budget": self.is_over_budget(),
        }
    
    def get_employees_info(self) -> List[Dict[str, object]]:
        """
        Get information about all employees.
        
        Returns:
            List[Dict[str, object]]: List of employee information.
        """
        return [emp.get_info() for emp in self.employees]
    
    def __str__(self) -> str:
        """String representation."""
        return f"Department({self.name}, {len(self.employees)} employees)"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (f"Department(name='{self.name}', manager_id='{self.manager_id}', "
                f"employees={len(self.employees)})")


from datetime import datetime
