#!/bin/python

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
        dp = 0
        for i in range(len(ar)):
            for j in range(len(ar)):
                if(((ar[i]+ar[j])%k == 0) and i < j):
                    dp+=1
    
        return dp



if __name__ == '__main__':


    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = map(int, raw_input().rstrip().split())

    result = divisibleSumPairs(n, k, ar)

