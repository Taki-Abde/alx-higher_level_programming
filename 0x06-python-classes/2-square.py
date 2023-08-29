#!/usr/bin/python3

# made by Megatron

"""Define a class Squar"""


class Square:
    """Represent a squar"""

    def __init__(self, size=0):
        """Initialize a new Squar

        Args:
            size (int): the size of the new squar
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
