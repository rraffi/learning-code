import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
# [1, 2, 3, 4, 3, 2, 1]
# 1: 2
# 2: 2
# 3: 2
# 4: 1

def lonelyinteger(a):
    # Write your code here
    d = {}
    res = -1

    for num in a:
        if num in d:
            d[num] += 1
        else:
            d[num] = 0

    for k, v in d.items():
        if v == 0:
            res = k

    return res


if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    print(result)
