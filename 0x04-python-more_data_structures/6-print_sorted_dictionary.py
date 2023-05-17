#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    diction = sorted(a_dictionary)
    for k, v in diction.items():
        print('{}: {}'.format(k, v))
