
import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

# middle-Outz

# s = [] //org
# r = []

# ASCII Solution

# def rotate_ascii_code(c, k):
#     return (ord(c) - 97 + k) % 26 + 97
#
# def caesarCipher(s, k):
#     # Write your code here
#     d = {}
#     rotated_str = ''
#
#     for char in s:
#         if char.isalpha():
#             d.update({char.lower(): chr(rotate_ascii_code(char.lower(), k))})
#
#     for char in s:
#         if char.isalpha():
#             if char.isupper():
#                 rotated_str += d[char.lower()].upper()
#             else:
#                 rotated_str += d[char]
#         else:
#             rotated_str += char
#
#     print(rotated_str)


def caesarCipher(s, k):
    l = "abcdefghijklmnopqrstuvwxyz"

    rotated_s = ''

    for c in s:
        if c.lower() in l:
            for i in range(len(l)):
                if c.islower() and c.lower() == l[i]:
                    rotated_s += l[(i+k)%26]
                elif c.isupper() and c.lower() == l[i]:
                    rotated_s += l[(i+k)%26].upper()
        else:
            rotated_s += c

    print(rotated_s)



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)