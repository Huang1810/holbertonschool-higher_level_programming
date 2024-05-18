#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))  # Expected output: Area: 9

try:
    print(my_square_1.size)  # This should raise an AttributeError
except Exception as e:
    print(e)  # Expected output: 'Square' object has no attribute 'size'

try:
    print(my_square_1.__size)  # This should raise an AttributeError
except Exception as e:
    print(e)  # Expected output: 'Square' object has no attribute '__size'

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))  # Expected output: Area: 25
