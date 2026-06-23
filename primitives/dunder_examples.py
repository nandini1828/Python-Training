def dunder_rewrites():
    """Provide example rewrites of standard operations using dunder methods."""
    return {
        "equal": (15).__eq__(15),
        "absolute": (-42).__abs__(),
        "contains": "Python".__contains__("Py"),
    }
