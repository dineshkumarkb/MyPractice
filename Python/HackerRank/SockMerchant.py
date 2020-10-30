#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d = {}
    count = 0
    for i in ar:
        d.setdefault(i,0)
        d[i]+=1

    for k,v in d.items():
        if(v//2 != 0):
            count+=(v//2)


    return count



if __name__ == '__main__':


    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

