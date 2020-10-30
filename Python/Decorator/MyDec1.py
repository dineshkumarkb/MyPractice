'''def emptylistcheck(mtd):
    print "Inside decorator"
    def checkforelements(self,l):
        if len(l) > 0:
            return mtd(self,l)
    return checkforelements


class MyDec1:

    @emptylistcheck
    def bsort(self,l):

        for i in xrange(len(l)):
            for j in xrange(len(l)-i-1):
                if l[j] > l[j+1]:
                    l[j],l[j+1] = l[j+1],l[j]

        return l


m = MyDec1()
l = [88,12,1,3,14,15,18,10,9,5,2]
print m.bsort(l)'''


def mydec(func):
    print "Inside mydec function"
    func
    print "After executing func()"
    return func


def testme():
    print "Inside testme function"


t = mydec(testme)()




