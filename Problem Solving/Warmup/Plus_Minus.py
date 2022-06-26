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

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zer = 0
    for i in arr:
        if i > 0:
            pos = pos + 1
        elif i < 0:
            neg = neg + 1
        else:
            zer = zer + 1
    fract_pos = pos / len(arr)
    fract_neg = neg / len(arr)
    fract_zer = zer / len(arr)
    print("{:.6f}".format(fract_pos))
    print("{:.6f}".format(fract_neg))
    print("{:.6f}".format(fract_zer))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
