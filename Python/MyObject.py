class MyObject(object):

    firstname = None
    lastname = None



    def __init__(self,TAG):

        self.TAG = TAG
        self.d = {}

    def __new__(cls,TAG):

        return object.__new__(cls)

    def __str__(self):

        return "This is a string version {}"

    def __getattr__(self, item):

        return self.__dict__[item]

    def __setattr__(self, key, value):

        self.__dict__[key] = value

    def __getitem__(self, item):

        return self.d[item]

    def __setitem__(self, key, value):

        self.d[key] = value


class Factory:

    def createobject(self):

        m = MyObject("Factory Class")
        m["Dinesh"] = 1
        print m["Dinesh"]
        MyObject.firstname = "Dinesh"
        MyObject.lastname = "Kumar"

        Retrive.getValues()

class Retrive:


    @staticmethod
    def getValues():

        print MyObject.firstname + " " + MyObject.lastname

if __name__ == "__main__":

    f = Factory()
    f.createobject()


