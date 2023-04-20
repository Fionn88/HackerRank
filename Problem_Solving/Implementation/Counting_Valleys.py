"""
如有走過山谷必是往上走，並走到海平面，即是一個山谷
"""




#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    count = 0
    valley = 0
    for i in path:
        if i == 'U':
            count += 1
            if count == 0:
                valley += 1
        elif i == 'D':
            count -= 1
    return valley
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
