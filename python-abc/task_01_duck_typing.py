#!/usr/bin/python3
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initialize a circle with a given radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return 3.141592653589793 * self.radius**2

    def perimeter(self):
        """Calculate and return the perimeter of the circle."""
        return 2 * 3.141592653589793 * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initialize a rectangle with given width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            The area of the rectangle (width x height).
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle (2 x (width + height)).
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape using duck typing.

    Args:
        shape: Any object that has area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
