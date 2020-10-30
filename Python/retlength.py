def retlength(mylist):
    count = 0
    for i in mylist:
        count+=1
    return count



l = [i for i in range(100000)]
print retlength(l)