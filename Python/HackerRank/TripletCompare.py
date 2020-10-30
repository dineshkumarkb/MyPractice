#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
        else:
            pass
    return [alice,bob]


if __name__ == '__main__':

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    result = solve(a, b)

    print result

