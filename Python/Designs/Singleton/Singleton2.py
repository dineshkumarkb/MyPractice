class Singleton2(object):

    __instance = None


    def __init__(self):
        pass

    def __new__(cls):

        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def getObject(self):

        return self



s = Singleton2()
print s.getObject()

s1 = Singleton2()
print s1.getObject()




