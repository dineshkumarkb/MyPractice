# Program to demonstrate __call__ function

class CallMe(object):

    count = 0

    def __init__(self):
        print " Inside init "

    def __call__(self, name):
        print " Called from {} ".format(name)
        CallMe.count+=1

    def getCount(self):

        return CallMe.count


class Called(object):

    def __init__(self):

        self.obj = CallMe()


    def callFunc(self):

        self.obj(self.__class__.__name__)

    def __repr__(self):
        repr()

c = Called()
c.callFunc()
