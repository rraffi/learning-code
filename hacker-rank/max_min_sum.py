import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # max_sum = min_sum = sum(arr[:-1])
    #
    # for num in arr:
    #     temp_arr = arr.copy()
    #
    #     if num in temp_arr:
    #         temp_arr.remove(num)
    #     max_sum = max(max_sum, sum(temp_arr))
    #     min_sum = min(min_sum, sum(temp_arr))

    print(sum(arr) - max(arr), sum(arr) - min(arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
