#!/usr/bin/python3
"""define a function that rpints square"""
def print_square(size):
    """Prints squares
    Args:
        size (int): The size of the square
    Raises:
        TypeError: If size is not int
        ValueError: If size is negative number
        TypeError: If size is float and less then zero
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size, end='')
        print()
