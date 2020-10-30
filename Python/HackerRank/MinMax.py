import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
   l = []
   for i in range(1,len(arr)+1):
       print arr[i:] + arr[:i-1]
       l.append(sum(arr[i:] + arr[:i-1]))

   print min(l),max(l)



if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())
    # s = sum(arr)
    # print s-max(arr)
    # print s-min(arr)
    miniMaxSum(arr)
