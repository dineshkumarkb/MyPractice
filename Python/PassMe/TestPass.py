class TestPass:

    a = 10
    b = 20

    def testcall(self):
        self.passcall(self.a,self.b)

    def getAValue(self):

        return self.a

    def getBValue(self):

        return self.b

    def passcall(self,a,b):
        self.a = self.a + 10
        self.b = self.b + 10
        print " The value of a inside passcall is ", self.a
        print " The value of b inside passcall is ", self.b



t = TestPass()
t.testcall()
print t.getAValue()
print t.getBValue()