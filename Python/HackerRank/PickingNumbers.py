#!/bin/python

import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(a):
    count = 0
    l = []
    for i in range(len(a)):
        for j in range(len(a)-1):
            if(abs(a[j]-a[j+1]) <= 1):
              l.append(a[i])
              count+=1


    print l



if __name__ == '__main__':

    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    result = pickingNumbers(a)


