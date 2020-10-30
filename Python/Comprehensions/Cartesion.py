from datetime import datetime

class Cartesian(object):

    def __init__(self,a,b):
        assert isinstance(a,list), " The variable a is not a list "
        assert isinstance(b,list), " The varible b is not a list "
        self.a = a
        self.b = b
        print " {0} Calling cart_comprehension ".format(datetime.now())
        self.cart_comprehension()
        print " {0} After Calling cart_comprehension ".format(datetime.now())
        print " {0} Calling cart_loop ".format(datetime.now())
        self.cart_loop()
        print " {0} After Calling cart_loop ".format(datetime.now())

    def cart_comprehension(self):

        print [(i,j) for i in self.a for j in self.b]

    def cart_loop(self):

        for i in self.a:
            for j in self.b:
                print (i,j)

a = [[1,2],
     [3,4]]

b = [[5,6],
     [7,8]]
c = Cartesian(a,b)