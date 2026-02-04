#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise TypeError("area() is not implemented")

    def integer_validator(self, name, value):
        