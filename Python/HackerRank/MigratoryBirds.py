#!/bin/python

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(ar):

    d = {}

    for i in ar:
        d.setdefault(i,0)
        d[i]+=1
    mymax = max([k for k in d.values()])
    for k,v in d.items():
        if v == mymax:
            print k



if __name__ == '__main__':

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = migratoryBirds(ar)


