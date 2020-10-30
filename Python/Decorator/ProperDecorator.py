''' Generic form of decorators
****This code will be helpful to understand
****the decorators functioning.
****Decorators without arguments

def outerdecorator(func_tobe_decorated):
    def wrapper(*args,**kwargs):
        do something with the args passed if you want
        return func_tobe_decorated(*args,**kwargs)
    return wrapper

@outerdecorator

The below function call can be written as

outer_dec = outer_dec(passfunction)


'''

def outer_dec(func):
    print " Inside outer_dec ", func
    def wrapper(*args):
        print " Inside wrapper before returning function "
        return func(*args)
    return wrapper


class ProperDecorator(object):

    def __init__(self):
        pass

    @outer_dec
    def passfunction(self,arg1,arg2):
        print " Inside passfunction "
        print " arg1 = ", arg1
        print " arg2 = ", arg2


p  = ProperDecorator()
p.passfunction(23,42)

''' The below given code snippet is the function equivalent of a decorator '''

# def passfunction():
#     print " Inside passfunction "
#
# outer_dec(passfunction)()