#!/usr/bin/python3
"""Define a function to ssay name"""


def say_my_name(first_name, last_name=""):
    """Says a name
    Args:
        first_name (str): User first name
        liast_name (str): User last name
    Raises:
        TypeError: if first or last name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
