from collections import namedtuple
n = input()
cols = raw_input().split()
marks = namedtuple("marks","m")
ssum = 0
for i in range(n):
    ssum += int(raw_input().split()[cols.index("MARKS")])
print "%.2f" % (ssum/float(n))