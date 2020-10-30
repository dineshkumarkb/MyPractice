from collections import OrderedDict

n = input()
d = OrderedDict()


for i in range(n):
    myitems = raw_input().split()
    mykey = " ".join(myitems[:-1])
    myvalue = int(myitems[-1])
    d.setdefault(mykey,0)
    d[mykey] += myvalue


for k,v in d.items():
    print k,v
