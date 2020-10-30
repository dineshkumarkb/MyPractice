class MyName(object):

    def __init__(self,fname,lname):

        self.fname = fname
        self.lname = lname

    def __new__(cls,fname,lname):
       instance =  object.__new__(cls)
       print instance
       return instance




m = MyName("Dinesh","Kumar")
#print m


