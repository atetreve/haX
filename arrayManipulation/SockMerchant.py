#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colors = set(ar)

    pairs = 0

    for color in colors:
        if ar.count(color) % 2 == 0:
            pairs += ar.count(color) / 2
        if ((ar.count(color) - 1) % 2 == 0) and not (ar.count(color) == 1):
            pairs += (ar.count(color) - 1) / 2
    return pairs
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
