from itertools import groupby
s =  raw_input()
for i,j in groupby(s,lambda s:s[0]):
    print "({}, {})".format(len(list(j)),i),