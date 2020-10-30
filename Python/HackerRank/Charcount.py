from collections import Counter,defaultdict
s = raw_input()
print Counter(s)
d = {}
for i in s:
    d.setdefault(i,0)
    d[i]+=1

d1 = defaultdict(int)
for i in s:
    d1[i]+=1


print d1

