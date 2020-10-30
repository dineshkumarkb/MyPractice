def testmethod(obj):

    def changeargs(self,a, b):
        print obj.__name__ + " was called"
        print a,b
        if(b > a):
            a,b = b,a
        return obj(self,a,b)

    return changeargs


class MyDec:

    def __init__(self):

        print "This is just a test to see the functionality of a decorator"

    @testmethod
    def sum(self,a,b):

        return a + b


    @testmethod
    def difference(self,a,b):

        return a - b



m = MyDec()
print m.sum(10,20)
#print m.difference(10,20)