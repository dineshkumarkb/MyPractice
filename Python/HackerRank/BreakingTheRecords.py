#!/bin/python

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mymin = scores[0]
    mymax = scores[0]
    mincount = 0
    maxcount = 0
    for i in range(len(scores)):
        if(scores[i] < mymin):
            mymin = scores[i]
            mincount+=1

        if(scores[i] > mymax):
            mymax = scores[i]
            maxcount+=1

    return maxcount,mincount

if __name__ == '__main__':


    n = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    result = breakingRecords(scores)

    print result


