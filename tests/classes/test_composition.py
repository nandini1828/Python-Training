"""Test suite for composition classes."""
import pytest
from app.classes import Address, Office, Company


class TestAddress:
    def test_address_creation(self):
        addr = Address("123 Main St", "Springfield", "IL", "62701")
        assert addr.street == "123 Main St"
        assert addr.city == "Springfield"
        assert addr.state == "IL"
    
    def test_full_address(self):
        addr = Address("123 Main St", "Springfield", "IL", "62701")
        full = addr.get_full_address()
        assert "123 Main St" in full
        assert "Springfield" in full


class TestCompany:
    def test_company_creation(self):
        addr = Address("100 Tech Ave", "San Francisco", "CA", "94105")
        company = Company("TechCorp", addr)
        assert company.name == "TechCorp"
        assert len(company.offices) == 1
    
    def test_add_office(self):
        addr1 = Address("100 Tech Ave", "San Francisco", "CA", "94105")
        company = Company("TechCorp", addr1)
        
        addr2 = Address("200 Code St", "New York", "NY", "10001")
        office = Office("NY01", addr2)
        company.add_office(office)
        
        assert len(company.offices) == 2
