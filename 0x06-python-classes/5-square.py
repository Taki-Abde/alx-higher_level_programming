#!/usr/bin/python3

# Made by MEGATRON

"""Define a class Squar"""


class Square:
    """Represent a squar"""

    def __init__(self, size):
        """Init new squar

        Args:
            size (int): The size of the new squar
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the squar"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of the squar"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print squar with the # char"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
