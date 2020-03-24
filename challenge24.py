#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s[0].upper() + s[1:]
    for i in range(1,len(s)-1):
        if(s[i] == ' '):
            s = s[:i+1]+ s[i+1].upper()+ s[i + 2:]
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
