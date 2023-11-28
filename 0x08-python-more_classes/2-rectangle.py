#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):

        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return (self.__width)

    @width.setattr
    def width(self, value):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return (self.__height)

    def height(self, value):
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""

        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""

        if self.__height == 0 or self.__width == 0:
            return (0)

        return ((self.__height + self.__width) * 2)
