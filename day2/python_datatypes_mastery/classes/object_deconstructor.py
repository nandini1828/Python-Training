"""
Recursive object deconstructor
"""


def deconstruct_object(obj):

    if hasattr(obj, "__dict__"):

        return {
            key: deconstruct_object(value)
            for key, value in obj.__dict__.items()
        }

    elif isinstance(obj, list):

        return [deconstruct_object(item) for item in obj]

    return obj