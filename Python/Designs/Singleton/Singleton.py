""" This program is an example for one of the implementations of singleton"""

class Singleton:

    instance =  None

    def __init__(self):

        if self.instance is not None:
            raise ValueError, "Cannot be instantiated"

    @classmethod
    def getInstance(cls):

        if cls.instance is None:
            cls.instance = Singleton()
        return cls.instance

    def printme(self):

        print "This is from a singletone design pattern"

myinstance = Singleton.getInstance()
myinstance.printme()