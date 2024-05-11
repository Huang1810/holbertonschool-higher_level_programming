#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
n = abs(number) % 10
if number < 0:
    n = n * -1
if n > 5:
    print('Last digit of %d is %d and is greater than 5' % (number, n))
elif n == 0:
    print('Last digit of %d is %d and is 0' % (number, n))
else:
    print('Last digit of %d is %d and is less than 6 and not 0' % (number, n))
