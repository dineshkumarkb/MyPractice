class MyTest(object):


    def __init__(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs


    def add_me(self,arg1,arg2):

        if type(arg1) is not int or type(arg2) is not int:
            raise (TypeError,"arg1 and arg2 should be an int")

        return arg1+arg2

    def sub_me(self,arg1,arg2):
        pass






m = MyTest()
print(m.add_me(1,2))
