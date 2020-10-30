'''def mydec(args):
    def method1(name):
        name1 = "The give name is {} ".format(name)
        return name1

    return method1

@mydec
def getmystring(name):
    pass

print getmystring("Dinesh")


def singleton(classname):
    print classname.__name__ + " has been called"
    instances = {}

    def getInstance():

        if classname not in instances:
            instances[classname] = classname()

        return instances[classname]

    return getInstance


@singleton
class Test:

    def __init__(self):

        self.count = 0

    def inc(self):

        print "Inside inc"

        self.count+=1


m = Test()
m.inc()


'''

class Singleton(object):

    ''' Though we create objects multiple times it will always refer to the first created object'''

    __instance = None

    def __new__(cls):

        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        #else:
        #    cls.__instance.test = value

        return cls.__instance
    def printme(self,obj):

        print obj


s =  Singleton()
print s
s.printme("s")

s1 =  Singleton()
print s1
s1.printme("s1")

s2 =  Singleton()
print s2
s2.printme("s2")













