#!/usr/bin/python3
for i in range(0, 10):
    for k in range(0, 10):
        if i == 9 and k == 9:
            print('{}{}'.format(i, k))
        else:
            print('{}{}'.format(i, k), end=', ')
