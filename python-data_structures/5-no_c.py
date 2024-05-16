#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for chr in my_string:
        if chr != 'c' and chr != 'C':
            str += chr
    return str
