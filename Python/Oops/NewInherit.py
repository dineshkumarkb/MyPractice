"""
This piece of code is to learn tht any argument passed to __init__ should be passed
to new as well. Else during inheritance we may run into trouble.
"""


class A(object):

    def __init__(self,classname):
        print " init in A called ", classname
        if(classname is not None):
            self.classname = classname
        else:
            self.classname = self.__class__.__name__


    def __new__(cls, classname):

        return super(A,cls).__new__(cls)


class B(A):

    def __init__(self,classname):
        print " init in B called "
        super(B, self).__init__(self.__class__)

    def __new__(cls, classname):

        return super(B, cls).__new__(cls,classname)



b = B("test class name")
