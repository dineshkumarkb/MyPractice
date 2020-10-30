def ssort(mylist):

    for i in range(len(mylist)):
        min = i
        for j in range(i+1,len(mylist)):
            if mylist[j] < mylist[min]:
                min = j

        mylist[i],mylist[min] = mylist[min],mylist[i]

    return mylist

l = [87,45,32,1,90,400,45,87,34,1]
print ssort(l)