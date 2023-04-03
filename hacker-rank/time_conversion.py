import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hh = int(s[:2])
    msec = s[2:8]
    hh = hh % 12 if s[-2:] == 'AM' else hh % 12 + 12
    print(f'{hh:02}{msec}')

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
    # print(result)
