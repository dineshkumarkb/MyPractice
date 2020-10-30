from abc import abstractmethod

class Animal(object):

    def __init__(self):
        print (" Inside initializer of Animal class ")

    # def __new__(cls, *args, **kwargs):
    #     print " Inside constructor of Animal class "
    #     return super(Animal, cls).__new__(cls)

    @abstractmethod
    def makeNoise(self):
        pass

class Dog(Animal):

    def __init__(self):
        super(Dog, self).__init__()
        print (" Inside initializer of Dog class ")

    # def __new__(cls, *args, **kwargs):
    #     #super(Dog, cls).__new__(cls)
    #     print " Inside constructor of Dog class "
    #     return super(Dog,cls).__new__(cls)

    def makeNoise(self):
        print (" Inside make noise of Dog ")


d = Dog()

A = d
A.makeNoise()





