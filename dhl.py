#!/usr/bin/python3

import sys
string = "2.2, 1.3, 8.8, 5.5, 3.4, 12.5, 9.9, 2.7, 7.1, 1.1"

def numbers(num_string):
    num_list = num_string.split(', ')
    num_list_float = []

        num_list_float.append(floet(number))

        num_list_float.sort()

    print(num_list_float)

    if __name__ == "__main__":

        numbers(sys.argv[1])
