import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s, d, m):
    count = 0
    for i in range(len(s)):
        if(sum (s[i:m+i]) == d):
            count+=1

    return count




if __name__ == '__main__':

    n = int(raw_input())

    s = map(int, raw_input().rstrip().split())

    dm = raw_input().split()

    d = int(dm[0])

    m = int(dm[1])

    result = solve(s, d, m)

