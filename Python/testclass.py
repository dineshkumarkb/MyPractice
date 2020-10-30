class TestClass:


    def __init__(self,n):

        print "Inside constructor"
        print n

    @classmethod
    def myclassmethod(cls,n):
        print n
        mystring = cls(str(n))
        print mystring

    @staticmethod
    def mystaticmethod(n):
        print n

    def myinstancemethod(self,n):
        print n


t = TestClass(1)
TestClass.myclassmethod(15)
TestClass.mystaticmethod(10)
