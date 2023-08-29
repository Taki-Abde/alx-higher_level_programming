#!/usr/bin/python3

# Made by MEGATRON

"""8 Print Square instance"""


class Square:
    """ the class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """the Getter for size"""
        return self.__size

    @property
    def position(self):
        """the Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """the Setter for position"""
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        """the Setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """the Return of current squar"""
        return self.__size ** 2

    def my_print(self):
        """the Print squar using # taking into account position"""
        if not self.size:
            print()
            return

        print("\n" * self.position[1], end="")
        print("\n".join([" " * self.position[0] +
                        "#" * self.size
                         for i in range(self.size)]))

    def __str__(self):
        return f"" if not self.size else (
                f"\n" * self.position[1] +
                f"\n".join([" " * self.position[0] +
                            "#" * self.size
                            for i in range(self.size)]))
