#!/usr/bin/python3
def is_lower(c):
    if c == '':
        return False
    if ord(c) in range(97, 123):
        return True
    else:
        return False
