'''class Singleton1(object):

    __Instance = None

    def __new__(cls):

        print cls
        if not Singleton1.__Instance:
            Singleton1.__Instance = object.__new__(cls)

        return Singleton1.__Instance


    def printme(self,objname):

        print objname


s = Singleton1()
s.printme(s)

s1 = Singleton1()
s1.printme(s1)'''



class Singleton2:

    __Instance =  None

    class __Inner:

        def __init__(self):
            pass

        def printme(self):

            print "Inside inner class"

        def __str__(self):
            return repr(self)



    def __init__(self):

        if not Singleton2.__Instance:
            Singleton2.__Instance = Singleton2.__Inner()

    def __getattr__(self, item):

        return getattr(self.__Instance,item)


s = Singleton2()
s1 =  Singleton2()
print s.printme()
print s1.printme()