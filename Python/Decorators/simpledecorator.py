def external(func):

    def internal(a,b):
        a = a + 5
        b = b + 5
        return func(a,b)

    return internal


@external
def addition(a,b):
    return a+b


print(addition(1,5))



def yell(mystr):
    return mystr.upper()

print(yell("Hi"))



def greet(func):
    resp = func("Hello..meaow")
    print(resp)

greet(yell)