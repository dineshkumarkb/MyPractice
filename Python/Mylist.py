'''def ReturnmyList(mydict):

    return ["%s" % d for d in mydict]



mydict = ["Dinesh","Sarath","Kedar","Nirvaid"]
print ReturnmyList(mydict)

from dictsort import sortme


d = {"Company":"Symphony","Phone":"1500","Desig":"SSE"}

s = sortme()
print s.mysort(d)

l = []

print "\n".join([m for m in dir(l)])


l = ["Din","Tan","Man","Ran"]

getattr(l,"append")("Wan")
print l
print type(getattr(l,"pop"))

l = []
if callable(l.append):
    print "Callable"

def f1(x):

    return x+1

print f1(2)

print f1.__doc__

#a = (lambda x: x+1)
#print a(3)


class MySet:

    def __init__(self):

        self.l = []
        __testname1__ = "__testname1__"
        __testname2__ = "__testname2__"


    def myadd(self,a,b):
        return a + b

    def mysub(self,a,b):
        return a - b



m = MySet()
setattr(m, '__testname1__' ,m.myadd.__name__)
setattr(m,'__testname2__',m.mysub.__name__)

print getattr(m,"__testname1__",None)
print getattr(m,"__testname2__",None)


class TestPrivate:

     def __init__(self):
         pass

     def __printme(self):
         print "Inside private"

     def printme1(self):
         print "Inside public"


t = TestPrivate()
t._TestPrivate__printme()



import os

def getdir(path):

    mydirlist = os.listdir(path)
    print mydirlist
    for elements in mydirlist:
        elesplit = elements.split(".")
        try:
            if ((elesplit[-1] == "zip") or (elesplit[-1] == "m3u8") or (elesplit[-1] == "BIN") or (elesplit[-1] == "msi") or (elesplit[-1] == "xlsx")):
                print elesplit
            else:
                print "{} is a folder name".format(elesplit)
        except IndexError, e:
            print "Caught an error", e




getdir(r'D:\\')

import re

s = "work 800.555.1212-5555"

mypattern = r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$'

s1 = re.search(mypattern,s)

print s1.group(0)






l1 = ["p","r","o","g","r","a","m","m","i","n","g"]
l2 = ["p","r","o","g","r","a","m","i","n","g"]

flag = 0

limit = min(len(l1),len(l2))

if l1 == l2:
    print 0

elif abs(len(l1)-len(l2)) == 1:
    #l1.sort()
    #l2.sort()
    print l1
    print l2
    # Forward comparison
    for i in range(limit):
        print "l1[i] = ", l1[i]
        print "l2[j] = ", l2[i]
        print "\n"
        if (l1[i] == l2[i] and (l1.index(l1[i]) == l2.index(l2[i]))):
            print "Inside if"
        else:
            print "Inside else\n"
            flag+=1
    for j in range(-1,-10,-1):
        print j,j-1
        print "l1[j] = ", l1[j]
        print "l2[j] = ", l2[j]
        print "\n"
        if ((l1[j] == l2[j]) or (l1[j] == l2[j-1])):
            print "Inside if of second for"
        else:
            flag+=1




else:
    print 2




l1 = ["p","r","o","g","r","a","m","m","i","n","g"]
l2 = ["p","r","o","g","r","a","m","i","n","g"]


l3 = ["p","o","k","e","r"]
l4 = ["p","o","k","e"]

z1 = zip(l1,l2)
z2 = zip(l3,l4)

print z1

for elements in z1:
    if elements[0] == elements[1]:
        print "matched"
    elif elements[0]!= elements[1] :
        print elements[1][1]
        print "matched"

    else:
        print "unmatched"



import numpy


def single_insert_or_delete(s1,s2):

    s1 = s1.lower()
    s2 = s2.lower()

    l1 = [i for i in s1] # convert the string into an array
    l2 = [j for j in s2] # convert the second string in an array

    if s1 == s2:
        flag = 0

    elif abs(len(s1)-len(s2)) == 1:
        if len(l2) > len(l1):
            l1,l2 = l2,l1
        print l1
        print l2
        l3 = list(numpy.in1d(l1,l2)) # This will compare the elements of 2 arrays and return bool values if values do not match
        print l3

        if l3.count(False) > 1:
            flag = 2
        else:
            flag = 1
    else:
        flag = 2

    return flag


print "Output-1 ", single_insert_or_delete("the","that")






s1 = "spoke"
s2 = "poke"

l1 = [i for i in s1] # convert the string into an array
l2 = [j for j in s2] # convert the second string in an array


l1.append(l2)
print l1

i = 0

flag = 0

if s1.lower() == s2.lower():
    print flag

limit = max(len(l1),len(l2))

for i in range(limit):
    for j in range(len(l2)):
            print i,j
            if l1[i] == l1[5][j]:
                print "matched"



import subprocess

subprocess.Popen(r'vlc --rate 5 D:\Mp4\1.mp4',shell = True)

'''





