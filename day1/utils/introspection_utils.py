"""
Introspection Utilities
"""


class IntrospectionUtility:

    @staticmethod
    def get_type(obj):
        return type(obj)

    @staticmethod
    def get_id(obj):
        return id(obj)

    @staticmethod
    def get_attributes(obj):
        return [
            attribute
            for attribute in dir(obj)
            if not attribute.startswith("_")
        ]