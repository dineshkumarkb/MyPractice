class Singleton:

    __Instance = None

    class __Inner:

        def __init__(self):
            pass

        def __str__(self):
            return repr(self)

        def printme(self):

            print "Dinesh from Inner class"

    def __init__(self):

        if Singleton.__Instance == None:
            Singleton.__Instance = Singleton.__Inner()

    def __str__(self):

        return repr(Singleton.__Instance)


    def __getattr__(self, item):

        return getattr(self.__Instance,item)



s = Singleton()
print s

s1 = Singleton()
print s1






