#!/usr/bin/python3

# Made by MEGATRON

"""Defines a locked class"""


class LockedClass:
    """
    Prevent user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
