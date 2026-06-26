"""
Composition Example

Demonstrates composition pattern where classes contain other objects.
"""

from typing import List, Dict, Optional
from datetime import datetime


class Address:
    """
    Represents a physical address.
    
    Attributes:
        street: Street address.
        city: City name.
        state: State/province.
        postal_code: Postal code.
        country: Country name.
    """
    
    def __init__(self, street: str, city: str, state: str,
                 postal_code: str, country: str = "USA"):
        """Initialize an Address."""
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
    
    def get_full_address(self) -> str:
        """
        Get formatted full address.
        
        Returns:
            str: Complete address string.
        """
        return f"{self.street}, {self.city}, {self.state} {self.postal_code}, {self.country}"
    
    def __str__(self) -> str:
        """String representation."""
        return self.get_full_address()
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (f"Address(street='{self.street}', city='{self.city}', "
                f"state='{self.state}', postal_code='{self.postal_code}')")


class Office:
    """
    Represents a company office with address and details.
    
    Attributes:
        office_id: Unique office identifier.
        address: Address object (composition).
        floor_count: Number of floors.
        capacity: Maximum employee capacity.
    """
    
    def __init__(self, office_id: str, address: Address,
                 floor_count: int = 1, capacity: int = 100):
        """Initialize an Office."""
        self.office_id = office_id
        self.address = address  # Composition
        self.floor_count = floor_count
        self.capacity = capacity
        self.employees: List[str] = []
    
    def add_employee(self, employee_id: str) -> bool:
        """Add employee to office."""
        if len(self.employees) < self.capacity and employee_id not in self.employees:
            self.employees.append(employee_id)
            return True
        return False
    
    def get_occupancy_rate(self) -> float:
        """Get occupancy percentage."""
        return (len(self.employees) / self.capacity) * 100
    
    def get_info(self) -> Dict[str, object]:
        """Get office information."""
        return {
            "office_id": self.office_id,
            "address": str(self.address),
            "floor_count": self.floor_count,
            "capacity": self.capacity,
            "current_employees": len(self.employees),
            "occupancy_rate": round(self.get_occupancy_rate(), 2),
        }


class Company:
    """
    Represents a company with multiple offices.
    
    Demonstrates composition with Office objects.
    """
    
    def __init__(self, name: str, headquarters_address: Address):
        """
        Initialize a Company.
        
        Args:
            name: Company name.
            headquarters_address: Address of headquarters.
        """
        self.name = name
        self.headquarters = Office("HQ", headquarters_address)
        self.offices: List[Office] = [self.headquarters]
        self.founded_date = datetime.now()
    
    def add_office(self, office: Office) -> bool:
        """
        Add new office.
        
        Args:
            office: Office to add.
            
        Returns:
            bool: True if added successfully.
        """
        if office.office_id not in [o.office_id for o in self.offices]:
            self.offices.append(office)
            return True
        return False
    
    def get_office(self, office_id: str) -> Optional[Office]:
        """
        Get office by ID.
        
        Args:
            office_id: Office ID.
            
        Returns:
            Optional[Office]: Found office or None.
        """
        for office in self.offices:
            if office.office_id == office_id:
                return office
        return None
    
    def get_total_capacity(self) -> int:
        """
        Get total employee capacity across all offices.
        
        Returns:
            int: Total capacity.
        """
        return sum(office.capacity for office in self.offices)
    
    def get_total_employees(self) -> int:
        """
        Get total employees across all offices.
        
        Returns:
            int: Total employee count.
        """
        return sum(len(office.employees) for office in self.offices)
    
    def get_company_info(self) -> Dict[str, object]:
        """
        Get comprehensive company information.
        
        Returns:
            Dict[str, object]: Company details.
        """
        return {
            "name": self.name,
            "headquarters": str(self.headquarters.address),
            "office_count": len(self.offices),
            "total_capacity": self.get_total_capacity(),
            "total_employees": self.get_total_employees(),
            "overall_occupancy": round(
                (self.get_total_employees() / self.get_total_capacity()) * 100, 2
            ),
        }
    
    def get_offices_info(self) -> List[Dict[str, object]]:
        """
        Get information about all offices.
        
        Returns:
            List[Dict[str, object]]: List of office information.
        """
        return [office.get_info() for office in self.offices]
    
    def __str__(self) -> str:
        """String representation."""
        return f"Company({self.name}, {len(self.offices)} offices)"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (f"Company(name='{self.name}', offices={len(self.offices)}, "
                f"employees={self.get_total_employees()})")
