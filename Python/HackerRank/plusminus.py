import math
import os
import random
import re
import sys
from fractions import Fraction

# Complete the plusMinus function below.
def plusMinus(arr):
    pcount = 0
    ncount = 0
    zcount = 0

    for i in arr:
        if(i < 0):
            ncount+=1
        elif(i > 0):
            pcount+=1
        else:
            zcount+=1
    print ('%.6f' % float((Fraction(pcount,len(arr)))))
    print ('%.6f' % float((Fraction(ncount,len(arr)))))
    print ('%.6f' % float((Fraction(zcount,len(arr)))))





if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)