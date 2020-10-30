#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the birthdayCakeCandles function below.

def birthdayCakeCandles(ar):

    # candle_count = 0
    #
    # for i in ar:
    #     if i == max(ar):
    #         candle_count+=1
    #
    # return candle_count
    return ar.count(max(ar))



if __name__ == '__main__':


    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = birthdayCakeCandles(ar)

    print result
