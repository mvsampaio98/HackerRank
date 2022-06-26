#!/bin/python3

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
    min_array = []
    max_array = []
    for i in arr:
        min_array.append(i)
        max_array.append(i)
    min_array.sort(reverse=False)
    max_array.sort(reverse=True)
    min_array.pop()
    max_array.pop()
    soma_min = sum(min_array)
    soma_max = sum(max_array)
    print(soma_min, soma_max)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
