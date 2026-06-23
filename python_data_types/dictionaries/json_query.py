"""
Simple nested dictionary query using dot notation.
"""


def query_json(data, path, default=None):
    """
    Example:
        data = {"user": {"name": "Alice"}}
        path = "user.name"
    """

    keys = path.split(".")
    current = data

    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default

    return current