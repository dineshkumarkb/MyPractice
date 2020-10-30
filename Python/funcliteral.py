class FuncLiteral(object):

    def __init__(self):
        self.testfunc = self.callme
        self.caller(self.testfunc)

    def callme(self):
        print " Inside callme "
        return " Callme is called "

    def caller(self,func1):
        print " Calling ", func1
        func1()



f = FuncLiteral()


