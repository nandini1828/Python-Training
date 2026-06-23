"""
Exercise Solutions - Section 1
"""


def dunder_rewrite():
    """
    Exercise 1.1
    Rewrite operations using dunder methods.
    """

    equality_result = (15).__eq__(15)

    absolute_result = (-42).__abs__()

    substring_result = "Python".__contains__("Py")

    return {
        "equality_result": equality_result,
        "absolute_result": absolute_result,
        "substring_result": substring_result
    }


class NamingConventionDemo:

    public_variable = "I am public"

    _internal_variable = "I am internal"

    __private_variable = "I am name mangled"

    def public_method(self):
        return "Public Method"

    def _internal_method(self):
        return "Internal Method"

    def __private_method(self):
        return "Private Method"


def demonstrate_naming_conventions():
    """
    Demonstrates Python naming conventions.
    """

    demo = NamingConventionDemo()

    return {
        "public_attributes": [
            item
            for item in dir(demo)
            if not item.startswith("_")
        ],
        "all_attributes": dir(demo)
    }