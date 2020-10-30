#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s, d, m):

    count = 0
    print s[1:m + 2]
    print s[1]
    #print s[1:m + 1]
    # for i in range(len(s)-1):
    #         # if((s[j] + s[j+1]) == d ):
    #         #    print [s[i],s[i+1]]
    #         #    count+=1
    #      print s[i:m + i]
    #
    # print count

if __name__ == '__main__':

    n = int(raw_input())

    s = map(int, raw_input().rstrip().split())

    dm = raw_input().split()

    d = int(dm[0])

    m = int(dm[1])

    result = solve(s, d, m)


