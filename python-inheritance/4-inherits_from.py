#!/usr/bin/python3
# This function checks if an object is an instance of a subclass (not the exact class)
def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a subclass of a_class (not the class itself).
    
    Args:
        obj: The object to check.
        a_class: The class to check against.
    
    Returns:
        True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return type(obj) != a_class and isinstance(obj, a_class)
