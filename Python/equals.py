class Equals:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        print self.x is self.y

    def checkequals(self, element1, element2):

        return element1 == element2

    def checkis(self,element1,element2):

        return  element1 is element2


e = Equals(1000,1000)
x = 1000
y = 1000
print x
print y
print id(x)
print id(y)
print e.checkequals(x,y)
print e.checkis(x,y)

