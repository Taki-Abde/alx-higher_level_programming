#!/usr/bin/python3

# Made By MEGATRON

"""10. ByteCode -> Python #5"""
import math


class MagicClass:
    """the init and define methods area and circumference"""
    def __init__(self, radius=0):
        """the init MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """the Calcul area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """the Calcul circumference"""
        return 2 * math.pi * self.__radius
