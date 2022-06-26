#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    stairs = n - 2
    count = 0
    for i in range(1, n):
        print(' ' * stairs, '#' * i)
        stairs -= 1
    print('#' * n)
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
