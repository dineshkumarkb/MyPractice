'''class QSort:

    def __init__(self):

        pass

    def sortme(self,mylist):

        self.less = []
        self.great = []
        self.same = []

        pivot = mylist[0]

        if len(mylist) > 1:
            for element in mylist:
                if element > pivot:
                    self.great.append(element)
                elif element < pivot:
                    self.less.append(element)
                else:
                    self.same.append(element)
            self.sortme(self.great)
            self.sortme(self.less)

            mylist1 = self.less + self.same + self.great
            return mylist1

        else:
            return mylist


l = [87,45,32,1,90,400,45,87,34,1]
q = QSort()
print q.sortme(l)





def qsort(l, start, end):

    if (start>=end):
        return

    pivot = (start+end)//2
    i,j = start,end

    while i <= j:

        while(l[i] < l[pivot]):
            #print "The l[i] value is", l[i]
            #print "The pivot value is", l[pivot]
            i+=1
        while(l[j] > l[pivot]):
            #print "The l[j] value is", l[j]
            #print "The pivot value is", l[pivot]
            j-=1
        if(i<=j):
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1
        #print l,start,j


    qsort(l,start,j)
    qsort(l,i,end)
    return l


a = [87,45,32,1,90,400,45,87,34]
print qsort(a,0,len(a)-1)




# Quick sort with extra memory space

def qsort(a):

    less = []
    equal = []
    great = []

    if len(a) > 1:
        pivot = a[0]
        for i in range(len(a)):
            if a[i] < pivot:
                less.append(a[i])
            elif a[i] > pivot:
                great.append(a[i])
            else:
                equal.append(a[i])

        return qsort(less)+equal+qsort(great)
    else:
        return a


a = [87, 45, 32, 1, 90, 400, 45, 87, 34]
print(qsort(a))



# Quick sort in place algorithm

import random

def qsort(a,start,end):

    print "start = ", start
    print "end = ", end

    if(start >= end):
        return a
    pivot = a[random.randint(start,end)]
    i,j = start,end
    while(i <= j):
        while(a[i] < pivot):
            i+=1
        while(a[j] > pivot):
            j-=1
        if(i <= j):
            a[i],a[j] = a[j],a[i]
            i+=1
            j-=1

    print "i , j ", i , j


    qsort(a,start,j)
    qsort(a,i,end)
    print a


a = [27,43,24,33,60,12]
qsort(a,0,len(a)-1)

'''

def ISort(l):

    i = 1

    while(i <  len(l)):
        j = i
        while(j > 0 and l[j] < l[j-1]):
            l[j],l[j-1] = l[j-1],l[j]
            j-=1

        i+=1
    print l

a = [87, 45, 32, 1, 90, 400, 45, 87, 34]
ISort(a)