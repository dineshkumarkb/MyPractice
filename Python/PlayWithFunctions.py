
# This method is to demonstrate that functions can be assigned to variables

def testme(name):

    return "Hello {}".format(name)

myvariable = testme

print myvariable("Dinesh")

# This is to demonstrate that functions can be written inside functions

def testme1(name):

    def callme():
        return "Hello"

    result = callme() + name
    return result

print testme1(" Dinesh")

# This is to demonstrate that functions can be passed as parameters

def testme2(name):

    return "Hello {}".format(name)

def func1(func):

    other_name = "Dinesh"
    return func(other_name)

print func1(testme2)
