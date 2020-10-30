from abc import abstractmethod,ABCMeta


class MyAbstractQueue:

    __metaclass__ = ABCMeta


    def __init__(self):
        pass

    @abstractmethod
    def put(self,element):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def getlength(self):
        pass

    @abstractmethod
    def putAll(self,mylist):
        pass

    @abstractmethod
    def emptyQueue(self):
        pass


for i in range(5):
    print i % 5