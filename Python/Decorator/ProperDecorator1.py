'''
This is another implementation of decorator as
we have implemented in autotouch. This approach can be used
if we are not going to do any changes in the arguments of the decorated function

def outerdecorator():
    def wrapper(func_tobe_decorated):
        do something with the args passed if you want
        return func_tobe_decorated
    return wrapper

@outerdecorator

'''

def outerdec(name):
    print " Inside outer dec ", name
    def wrapper(mtd):
        print " Inside wrapper "
        return mtd
    return wrapper

class ProperDecorator1(object):

    def __init__(self):
        pass

    @outerdec(name = "argofdecorator")
    def passfunction(self):
        print " Inside passfunction "


p = ProperDecorator1()
p.passfunction()