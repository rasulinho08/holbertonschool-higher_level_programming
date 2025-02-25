#!/usr/bin/python3
class BaseGeometry:
    """BaseGeometry class with methods for area calculation and integer validation."""

    def area(self):
        """Raises an Exception if area method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

