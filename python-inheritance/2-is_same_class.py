#!/usr/bin/python3
# This function checks if an object is exactly an instance of a given class
def is_same_class(obj, a_class):
    """
    Checks if obj is exactly an instance of the specified class.
    
    Args:
        obj: The object to check.
        a_class: The class to check against.
    
    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
