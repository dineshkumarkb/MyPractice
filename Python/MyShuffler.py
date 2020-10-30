import random

class MyShuffler(object):

    def __init__(self, mylist):

        self.mylist = mylist
        self.mylen = len(mylist)
        self.myrandom = random.Random()

    def main(self):

        for i in xrange(self.mylen):
            __myrandomvariable = self.myrandom.randrange(self.mylen)
            self.mylist[i],self.mylist[__myrandomvariable] = self.mylist[__myrandomvariable],self.mylist[i]

        return self.mylist

    def __getattr__(self, item):

        ''' Only called if the attribute is not found the usual ways. Else it is not called'''

        #object.__getattribute__(self,item)

        print "Inside getattr" , self.mylist

        if item == "__myrandomvariable":
            return "A random variable"

        else:
            raise AttributeError


l = [345,54,23,45,64,789,90]
m = MyShuffler(l)
print m.main()
print m.__myrandomvariable
