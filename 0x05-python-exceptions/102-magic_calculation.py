#!/usr/bin/python3

# Made by Megtron

def magic_calculation(a, b):
    rs = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            rs += a ** b / i
        except Exception:
            rs = b + a
            break
    return rs
