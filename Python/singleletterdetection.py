''' -- > Solution 1
import re
def isA(mylist):

    mypattern = r'^a.+'
    flag = None

    for s in mylist:
        if re.search(mypattern,s):
            return True
        else:
            flag = False
    return flag

l = ["bt","nt","aat"]
print isA(l)



# Solution 2

def isA(mylist):
    flag = None
    for i in mylist:
        if i.startswith("a"):
            return True
        else:
            flag = False
    return flag


l = ["bt","nt","t"]
print isA(l)


# Solution 3
def isA(mylist):

    return any(i.startswith("a") for i in mylist)


l = ["bt","nt","t"]
print isA(l)
'''

# Solution 4 The most simple

def isA(mylist):
    for s in mylist:
        if s.startswith("a"):
            return True
    return False

l = ["abt","nt","t"]
print isA(l)


