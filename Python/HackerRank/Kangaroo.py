#!/bin/python

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    k1_jump_count = 0
    k2_jump_count = 0
    answer = "NO"
    j = 0
    while(j < 10000):
        k1_pos = x1+v1
        k2_pos = x2+v2
        k1_jump_count += 1
        k2_jump_count += 1
        if(k1_pos == k2_pos and k1_jump_count == k2_jump_count):
            answer = "YES"
            break
        elif(x2 > x1 and v2 > v1):
            break

        x1, x2 = k1_pos, k2_pos
        j+=1

    print  answer




if __name__ == '__main__':


    x1V1X2V2 = raw_input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

