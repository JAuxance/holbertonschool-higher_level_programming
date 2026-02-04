#!/usr/bin/python3
# This function checks if an object is an instance of a class or its subclasses
def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or a subclass of a_class.
    
    Args:
        obj: The object to check.
        a_class: The class to check against.
    
    Returns:
        True if obj is an instance of a_class or a subclass, False otherwise.
    """
    return isinstance(obj, a_class)
