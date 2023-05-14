#!/usr/bin/python3
def no_c(my_string):
    if isinstance(my_string, str):
        new_str = ''
        for i in my_string:
            if i != 'c' in my_string and i != 'C':
                new_str += i
        return new_str
