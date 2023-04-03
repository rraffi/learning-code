#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def print_six_decimal_places(num):
    print(f'{num:.6f}')

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zeros = 0

    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zeros += 1

    print_six_decimal_places(pos/len(arr))
    print_six_decimal_places(neg/len(arr))
    print_six_decimal_places(zeros/len(arr))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
