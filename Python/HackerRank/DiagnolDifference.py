#!/bin/python

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):

    add1 = 0
    add2 = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
             if(i == j):
                 #print arr[i][j],
                 add1+=arr[i][j]
             if (j == len(arr) - 1 - i):
                  #print arr[i][j],
                 add2 += arr[i][j]

    if add2 > add1:
        add1,add2 = add2,add1

    return add1-add2

    # for k in range(len(arr)):
    #     for l in range(len(arr)):
    #         if(l == len(arr)-1-k):
    #             print arr[k][l],
    #     print




if __name__ == '__main__':


    n = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    print result

