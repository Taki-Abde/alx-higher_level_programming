#!/usr/bin/python3

# MADE BY MEGATRON

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list

    Args:
        my_list (list): list to print elements from
        x (int): num of elements of my_list to print

    Returns:
        num of elements printed
    """
    rt = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            rt += 1
        except IndexError:
            break
    print("")
    return (rt)
