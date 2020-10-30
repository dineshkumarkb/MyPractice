#!/bin/python

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):

    if(abs(x-z) > abs(y-z)):
        print "Cat B"
    elif(abs(x-z) < abs(y-z)):
        print "Cat A"
    else:
        print "Mouse C"

if __name__ == '__main__':

    q = int(raw_input())

    for q_itr in xrange(q):

        xyz = raw_input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

