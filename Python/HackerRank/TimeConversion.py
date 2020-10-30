#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):

    conv = s.split(":")

    hr = conv[0]
    conv[2] = conv[2].strip(s[-2:])

    if(s[-2] == "P" and int(hr) != 12):
        hr = int(hr)+12
        conv[0] = str(hr)
    elif(s[-2] == "A"):
        if(int(conv[0]) == 12):
            conv[0] = "00"

    return ":".join(conv)






if __name__ == '__main__':

    s = raw_input()

    result = timeConversion(s)

    print (result)


