#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    if len(my_list) == 0:
        return []
    for i, c in enumerate(my_list):
        if search == c:
            new_list.append(replace)
        else:
            new_list.append(c)
    return new_list
