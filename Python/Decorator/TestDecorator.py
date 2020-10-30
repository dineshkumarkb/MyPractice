def outer(func):
    print "Inside outer func"
    def inner(a,b):
        print "Inside inner"
        func(a,b)
        print "After func call"

    return inner

def decoratedFunction(a,b):

    print "Inside decorated function", a,b




outer = outer(decoratedFunction)
outer(2,5)