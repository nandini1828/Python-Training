"""
Test suite for PrimitiveManager class.
"""

import pytest
from app.primitive_datatypes import PrimitiveManager


class TestPrimitiveManager:
    """Test cases for PrimitiveManager."""
    
    def test_initialization(self):
        """Test manager initialization."""
        manager = PrimitiveManager()
        assert manager.integer_demo is not None
        assert manager.float_demo is not None
        assert manager.string_demo is not None
        assert manager.boolean_demo is not None
    
    def test_get_all_demonstrations(self):
        """Test getting all demonstrations."""
        manager = PrimitiveManager()
        all_demos = manager.get_all_demonstrations()
        
        assert "integer" in all_demos
        assert "float" in all_demos
        assert "string" in all_demos
        assert "boolean" in all_demos
    
    def test_get_demonstrations(self):
        """Test individual demonstration getters."""
        manager = PrimitiveManager()
        
        int_demos = manager.get_integer_demonstrations()
        assert "basic_operations" in int_demos
        assert "bitwise_operations" in int_demos
        
        float_demos = manager.get_float_demonstrations()
        assert "basic_operations" in float_demos
        
        string_demos = manager.get_string_demonstrations()
        assert "string_creation" in string_demos
        
        bool_demos = manager.get_boolean_demonstrations()
        assert "boolean_basics" in bool_demos
    
    def test_comparison_test(self):
        """Test comparison between types."""
        manager = PrimitiveManager()
        result = manager.run_comparison_test()
        
        assert result["int_equals_float"] is True
        assert result["true_equals_one"] is True
        assert result["false_equals_zero"] is True
