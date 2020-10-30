# Decorator example 1

def testdec(mtd):
    def wrapper():
        print "Inside the decorator before executing the function"
        mtd()
        print "Inside the decorator after executing the function"
    return wrapper



@testdec
def mydec2():
    print "Inside mydec2 function"


#mydec2()


# Passing arguments to the decorated function via the wrapper

def testdecwithargs(mtd):

    def wrapper(a,b):
        print "Inside the dec's wrapper"
        print "The args are"
        print a
        print b
        mtd(a,b)

    return wrapper



@testdecwithargs
def mydec2(a,b):
    print "Inside mydec2 function the args are %d %d" %(a,b)


#mydec2 = testdecwithargs(mydec2)
#mydec2(1,2)


# Passing arguments to decorated methods via class

def testmethod(func):
    def wrapper(self,fname,lname):
        func(self,fname,lname)
    return wrapper

class PrintName:


    @testmethod
    def displayname(self,fname,lname):
        print "Myfirstname is", fname
        print "MyLastname is", lname


#p = PrintName()
#p.displayname("Dinesh","Kumar")


# Passing arguments to the decorator per se


def testme(cap = None, bitrate = None):

    print "The capabilities are", (cap,bitrate)

    def mydecorator(func):
        def wrapper():
            print "Inside wrapper"
            return func()

        return wrapper
    return mydecorator




@testme(cap = "JWplayer",bitrate = True)
def method_tobe_decorated():
    print "Inside method to be decorated"

method_tobe_decorated()





# Program to demonstrate closure in python



def outer():
    x = 10
    #print "x in outer", x
    def inner():

        #print "x in inner", x

        return x
    return inner


#a = outer()
#print a()



def func1(f1,f2):
    print "Inside function1"
    f1()
    f2()



def func2():
    print "Inside func2"


def func3():
    print "Inside function3"


def outer(x):
    print "x inside outer", x
    def inner():
        print "x inside inner", x
    return x + 20

    inner()



#print outer(10)













