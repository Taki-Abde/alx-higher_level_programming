#!/usr/bin/python3

# Made By MEGATRON

"""7 Singly linked list"""


class Node:
    """
    the Class Node
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """the Data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """the Data setter"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """the next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """the Class SinglyLinkedList"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        string = ""
        tmp = self.__head

        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """the insert of values"""

        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        tmp = self.__head

        if new.data < tmp.data:
            new.next_node = self.__head
            self.__head = new
            return

        while tmp.next_node is not None and new.data > tmp.next_node.data:
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
        return
