#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10

if last == 0:
	adjective = '0'
elif last > 5:
	adjective = 'greater than 5'
else:
	adjective = 'less than 6 and not 0'
print("last digit of {} is {} and is {}".format(number, last, adjective))
