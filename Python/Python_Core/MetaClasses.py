"""
This is to demonstrate creation of classes using regular methods and using 'type'
object.The class which is created below can also be created using type which is demonstrated below the usual
method.

Metaclasses --> A class which defines how classes should work in python.
Why do we need this --> Because classes are objects in python. We need a way to define how classes should work.

Any object which has the capability to create objects is nothing but a class.

"""

# Creating classes - Method 1

class ClassCreator(object):

    def __init__(self):
        pass

    def get_instance(self):
        pass

print ClassCreator().__class__.__dict__
#print type(ClassCreator())

# Creating classes - Method 2 Using type
d = {'get_instance': '<function>'}
ClassCreator1 = type('ClassCreator1',(),d)
print ClassCreator1().__class__.__dict__