#!/usr/bin/python3

# Made by Megatron

def safe_function(fct, *args):
    import sys
    try:
        rs = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        rs = None

    return (rs)
