
def outer():
    print " Inside outer before inner "
    def inner(func):
        print " Inside inner "
        return func

    return inner




def func_tobe_decorated():
    print " Inside func to be decorated "


outer_return = outer()
outer_return(func_tobe_decorated)()