#!/usr/bin/python3

# Made by MEGATRON

def safe_print_integer(value):
    """Print an intg with "{:d}".format().

    Args:
        value (int): intg to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
