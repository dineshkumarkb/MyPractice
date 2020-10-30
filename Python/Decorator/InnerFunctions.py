def outerfunction(func):
    print "Inside outer function"
    def innerfunction():
        print "Inside inner function"
        func()
    return innerfunction




def testme():
    print "Inside the test me function"


testinnerfunctioncall = outerfunction(testme)
testinnerfunctioncall()