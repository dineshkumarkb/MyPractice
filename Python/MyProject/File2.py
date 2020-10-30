from File1 import *

class MyTest2(MyTest1):

    name = "Dinesh"


    def mul(self,a,b):

        return a * b

    def div(self,a,b):

        return a / b



if __name__ == "__main__":

    m = MyTest2()
    print m.mul(2,1)
    print m.div(2,1)
