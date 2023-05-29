#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
    except (TypeError, ZeroDivisionError):
        return None
    finally:
        print('{:d}'.format(res))
    return res
