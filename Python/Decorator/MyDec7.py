def testmethod(arg):
    print " Decorator args ", arg
    def wrap(func):
        print " Inside wrap "
        def interChangeValues(mtd,a,b):
            print " Inside interchange values ",func , mtd
            func(mtd,a,b)
        return interChangeValues
    return wrap

class TestCalc(object):

    def __init__(self):
        pass

    @testmethod("Decorator String")
    def add(self,a,b):
        print " Inside add ", a , b

        return a+b

    @testmethod("Decorator String")
    def sub(self,a,b):

        return a-b

    #@testmethod()
    def mul(self,a,b):

        return a * b

    #@testmethod()
    def div(self,a,b):

        return a/b


t = TestCalc()
print t.add(2,1)
#print t.sub(1,2)