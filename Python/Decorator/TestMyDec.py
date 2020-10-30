'''
Decorator is just another function which will take a function object.
Do something with the function object and then return the function which did something to the function object
In the below  example,

outer is a function which will take a function object --> outer will take testdec function object
inner is the function which does something to the function object and returns the decorated function
finally outer returns the inner function

'''



def outer(func):
    print " Inside outer ", func
    def inner(*args,**kwargs):
        print " The args are ", args,kwargs
        return func(*args,**kwargs)
    print "Before returning inner"
    return inner



# class TestDecorator(object):
#
#     def __init__(self):
#         pass
#
#     @outer
#     def testdec(self):
#         print " Inside testdec "



def func_to_dec(a,b):
    print " Inside func_to_dec ",a,b


func_to_dec = outer(func_to_dec)(1,2)