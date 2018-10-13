#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'numbersSquare' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER s
#

def numbersSquare(n, s):
    # Write your code here    
    a = [[0]*n for i in range(n)]
    a[0][0] = s
    
    k = 1

    while k < n:
        a[0][k] = a[k-1][0] + 1
        a[k][0] = a[0][k] + 2*k
        for j in range(k):
            if j !=0:
                a[k][j] = a[k][j-1] - 1

        for i in range(k):
            if i != 0:
                a[i][k] = a[i-1][k] + 1

        a[k][k] = a[k-1][k] + 1

        k += 1
        
    return a

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    s = int(first_multiple_input[1])
    
    a = numbersSquare(n, s)

    for row in a:
        print(" ".join(str(row[i]) for i in range(len(row))))
