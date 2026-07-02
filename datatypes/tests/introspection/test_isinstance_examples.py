"""Test suite for isinstance examples."""
import pytest
from datatypes.introspection import InstanceOfExamples


class TestInstanceOfAdvanced:
    def test_issubclass_examples(self):
        result = InstanceOfExamples.issubclass_examples()
        assert result["car_is_subclass_of_vehicle"] is True
        assert result["car_is_not_subclass_of_truck"] is True
    
    def test_checking_abstract_base_classes(self):
        result = InstanceOfExamples.checking_abstract_base_classes()
        assert result["list_is_sequence"] is True
        assert result["string_is_sequence"] is True
        assert result["dict_is_mapping"] is True
