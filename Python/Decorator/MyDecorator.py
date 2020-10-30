# class MyDecorator:
#
#     def func1(self, func):
#        print "Inside function 1 before func statement"
#        #func
#        print "Inside function 1 after func statement"
#        return func
#
#
#     def func_tobe_decorated(self):
#         print "Inside function to be decorated"
#
#
#
# m = MyDecorator()
# m.func1(m.func_tobe_decorated)()


# def func1(func):
#
#     print "Inside func1"
#
#     def func2(arg1,arg2):
#         print "Inside func2 before func call"
#         print arg1
#         print arg2
#         func(arg1,arg2)
#         print "Inside func2 after func call"
#
#     return func2
#
# @func1
# def func_dec(arg1, arg2):
#     print "Inside func to be decorated", arg1,arg2
#
# # func1 = func1(func_dec)
# # print func1.__name__
# # func1()
#
# func_dec("test","test1")


# def outerFunc(func):
#     print "Inside Outer Func"
#
#     def innerFunc():
#         print "Before the decorated func call"
#         func()
#         print "After the decorated func call"
#
#     return innerFunc
#
# @outerFunc
# def decorated():
#     print "Inside decorated"
#
# decorated()


def outer(func):
    print "Inside outer"
    def inner():
        print "Inside inner"
        func()
    return inner


def decorated():
    print "Inside decorated"

outer = outer(decorated)
outer()


