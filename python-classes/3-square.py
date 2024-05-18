#!/usr/bin/python3
"""
This module defines a class Square with a private attribute size, proper validation,
and a method to calculate the area.
"""

class Square:
    """
    A class that defines a square by its size.
    
    Attributes:
        __size (int): The size of the square (private).
    
    Methods:
        __init__(self, size): Initializes a new Square instance with the given size.
        area(self): Returns the current square area.
    """
    
    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.
        
        Args:
            size (int): The size of the square, defaults to 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """
        Returns the current square area.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
