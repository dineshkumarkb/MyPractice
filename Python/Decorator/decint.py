def outer(func):
    def inner(a,b):
        a,b = b,a
        return func(a,b)
    return inner



def sub(a,b):
    return a-b

o = outer(sub)
print o(1,2)