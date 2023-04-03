import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sum_primary = 0
    sum_secondary = 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == j:
                sum_primary += arr[i][j]
            if i + j == len(arr) - 1:
                sum_secondary += arr[i][j]

    print(sum_primary)
    print(sum_secondary)
    diff = sum_primary - sum_secondary
    return diff * -1 if diff < 0 else diff



if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

