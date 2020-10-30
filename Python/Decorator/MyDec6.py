def checkvalues(argsfordecorator):
    print " Inside check values ", argsfordecorator
    def inner(func):
        print " Inside inner "
        return func

    return inner





class Calc:

    def __init__(self):
        pass

    @checkvalues("argfordecorator")
    def add(self,a,b):
        return a + b

    # @checkvalues("argofcheckvalue")
    # def sub(self,a,b):
    #     return a-b


c = Calc()
print c.add(1,2)
print "\n"

def checkvalues(argsofcheckvalue):
    print " Inside checkvalues " + argsofcheckvalue
    def inner(func_tobe_dec):
        print " Inside inner "
        return func_tobe_dec
    return inner


def testdec():
    print " Test dec called "

checkvalues = checkvalues("myargs")
checkvalues(testdec)()