#!/usr/bin/python3
def uppercase(str):
    if str == '':
        print('{}'.formt(str))
        return
    result = ''
    for i in str:
        if ord(i) in range(97, 123):
            i = ord(i) - (ord('a') - ord('A'))
        result += chr(i)
    print('{}'.format(result))
