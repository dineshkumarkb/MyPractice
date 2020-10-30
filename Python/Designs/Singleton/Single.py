class Single:

    mydb = {}

    def __init__(self):

        self.name = None
        self.company = None


    def __getattr__(self, item):

        if item == "name":
            return self.__dict__[item]
        elif item == "company":
            return self.__dict__[item]
        else:
            raise AttributeError(item)


    def __setattr__(self, key, value):

        self.__dict__[key] = value


s =  Single()
s.name = "Dinesh"
s.company = "Harman"
print s.name
print s.company
print getattr(s,"test")






