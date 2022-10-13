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
    valleys = 0
    seaLevel = 0
    inValley = False
    for i in range(steps):
        if path[i] == 'U':
            seaLevel += 1
        elif path[i] == 'D':
            seaLevel -= 1
        if inValley and seaLevel == 0:
            valleys += 1
            inValley = False
        elif seaLevel < 0:
            inValley = True
        
        
    return valleys
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
