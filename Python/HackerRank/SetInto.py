# from __future__ import division
#
#
# def average(array):
#
#     s =  set(array)
#     return sum(s)/len(s)

from itertools import permutations

s = raw_input().split()
for i in sorted(list(permutations(s[0],int(s[1])))):
    print "".join(i)














if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result