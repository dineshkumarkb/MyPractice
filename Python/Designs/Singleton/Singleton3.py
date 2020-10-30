class Singleton3(object):

    __instance = None


    def __new__(cls):


        if not cls.__instance:

            cls.__instance = object.__new__(cls)

        return cls.__instance


    def getObject(self):

        return self



s = Singleton3()
print s.getObject()

s1 = Singleton3()
print s1.getObject()
