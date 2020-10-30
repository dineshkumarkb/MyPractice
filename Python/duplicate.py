'''def duplicate(mylist):
    d = {}
    for i in mylist:
        d.setdefault(i,mylist.count(i))
    print d




duplicate([1,2,3,1,4,5,6,3])

'''

def duplicate(mylist):
    d = {}
    for i in mylist:
        d.setdefault(i,0)
        d[i]+=1
    #for i in mylist:
    #    d[i]+=1

    return d


print duplicate([1,2,3,1,1,1,1,4,5,6,3])