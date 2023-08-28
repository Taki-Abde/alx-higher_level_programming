#!/usr/bin/python3

# Made by Megatron

def safe_print_division(a, b):
    """Return the division of a by b."""
    try:
        dv = a / b
    except (TypeError, ZeroDivisionError):
        dv = None
    finally:
        print("Inside result: {}".format(dv))
    return (dv)
