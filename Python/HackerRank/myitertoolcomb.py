from itertools import combinations,combinations_with_replacement

s,n = raw_input().split()
for i in combinations_with_replacement(sorted(s),int(n)):
    print "".join(i)