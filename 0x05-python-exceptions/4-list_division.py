#!/usr/bin/python3

# Made by Megatron

def list_division(my_list_1, my_list_2, list_length):
    """Divides 2 lists element by element.

    Args:
        my_list_1 (list): 1st list.
        my_list_2 (list): 2sec second list.
        list_length (int): num of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            dv = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            dv = 0
        except ZeroDivisionError:
            print("division by 0")
            dv = 0
        except IndexError:
            print("out of range")
            dv = 0
        finally:
            new_list.append(dv)
    return (new_list)
