from __future__ import print_function

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    summ = 0
    for i in ar:
        summ+=i
    return summ



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = simpleArraySum(ar)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()

