#!/usr/bin/python3
"""Module 8-class_to_json"""


def class_to_json(obj):
    """dictionary representation for JSON serialization of
    an object
    Args:
        obj: object of a class
    Returns: dictionary description with simple data structure 
        for JSON serialization of an object
    """
    if isinstance(obj, (str, int, bool)):
        return obj

    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value
                in obj.items()}
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif hasattr(obj, '__dict__'):
        return class_to_json(obj.__dict__)
