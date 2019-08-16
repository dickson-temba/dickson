'''This is a "shebang"'''
#!usr/bin/python3

import sys
import os

def circle_info(radius):
    r = float(radius)
    pi = 3.14
    area = pi*(r**2)
    perimeter = 2*pi*r

    print("The area of the circle is: ", area)
    print("The perimeter of the circle is: ", perimeter)
    return(area)
def say_something(something):
    print(str(something))

if __name__ == "__main__":

    circle_info(sys.argv[1])

    circle_info(sys.argv[2])
