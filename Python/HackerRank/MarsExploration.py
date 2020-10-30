#!/bin/python

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    count = 0
    i = 0
    signal = ["S","O","S"]
    while(i < len(s)):
        sa = s[i:i+3]
        for j in range(len(sa)):
            if(sa[j] != signal[j]):
                count+=1

        i+=3
    return count


if __name__ == '__main__':


    s = raw_input()

    result = marsExploration(s)

