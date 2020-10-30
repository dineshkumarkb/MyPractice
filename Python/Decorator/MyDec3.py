'''def func1(mtd):
    print "Inside func1"
    def func2():
        print "Inside func2 before executing the decorated function"
        mtd()
        print "Inside func2 after executing the decorated function"
    return func2


#@func1
def method1():
    print "Inside method1"



mtd_dec = func1(method1)
print mtd_dec()


def f1():
    print "This is inside the function f1"
    def f2():
        print "This is inside the function f2"

    return f2


f = f1()
f()'''

def func1(func3):
    print "Inside func1"
    def func2():
        print "Inside func2 before executing func3"
        func3()
        print "Inside func2 after executing func3"

    return func2

def func3():
    print "Inside func3"

func3 = func1(func3)
func3()


