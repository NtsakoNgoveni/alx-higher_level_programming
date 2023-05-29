#!/usr/bin/python3
def safe_print_integer(value):
    truthy = True
    try:
        print('{:d}'.format(value))
    except ValueError:
        truthy = False
    return (truthy)
