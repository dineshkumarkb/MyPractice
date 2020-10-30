class MySingleton(object):

    __instance = None

    def __new__(cls, *args, **kwargs):

        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            print cls.__instance

        return cls.__instance

    def printmyname(self,name):

        print "The name is : ", name
        print "The repr is ", repr(self)
        var1 =  None
        if not var1:
            print "Inside if"



m = MySingleton()

m.printmyname("Dinesh")

m1 = MySingleton()
print m1
m1.printmyname("Kumar")