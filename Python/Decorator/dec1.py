def outer(func):
    print "Outer"
    def inner(arg1,arg2):
        print "Inner"
        arg1,arg2 = arg2,arg1
        return func(arg1,arg2)
    print "returning inner"
    return inner


@outer
def test_func(a,b):
    return a+b


print test_func(2,1)