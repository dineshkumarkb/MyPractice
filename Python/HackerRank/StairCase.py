#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    numbers = n-1
    for i in range(1,n+1):
        print (" " * numbers) + ("#" * i)
        numbers-=1


if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)