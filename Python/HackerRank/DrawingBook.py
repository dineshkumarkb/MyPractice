#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if abs(n-p) <= 1:
        print (0)



if __name__ == '__main__':

    n = int(raw_input())

    p = int(raw_input())

    result = pageCount(n, p)


