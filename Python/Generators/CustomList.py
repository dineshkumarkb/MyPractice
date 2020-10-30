class CustomList(object):

    def __init__(self):
        self.testlist = []

    def __getitem__(self, item):
        print " __getitem__ called ", item
        if(item == 0):
            return


    def __setitem__(self, key, value):
        print " __setitem__"
        self.testlist[key] = value


    def __getattribute__(self, item):
        print "__getattribute__"
        return object.__getattribute__(self,item)


    def __setattr__(self, key, value):
        print "__setattr__"
        self.__dict__[key] = value

    def __getattr__(self, item):
        print " No attribute found "
        self.__setattr__(item,0)



c = CustomList()
print c.a
print c.a



