#!/usr/bin/python3
def remove_char_at(str, n):
    c = ""
    for a in range(len(str)):
        if a != n:
            c = c + str[a]
    return (c)
