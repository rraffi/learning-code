#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

# Input string
# # ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']
# 0 0
# 1 0

def check_col_order(str_arr) -> str:
    i = 0
    n = len(str_arr)

    while i < n:
        for j in range(n - 1):
            print(f'({str_arr[j][i]},   {str_arr[j + 1][i]})')
            if str_arr[j][i] > str_arr[j + 1][i]:
                return 'NO'
        i = i + 1

    return 'YES'


def gridChallenge(grid):
    # Write your code here
    n = len(grid[0])
    print(grid[0])

    for i in range(n):
        sorted_string = ''.join(sorted(grid[i]))
        grid[i] = sorted_string

    res = check_col_order(grid)
    return res


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)

