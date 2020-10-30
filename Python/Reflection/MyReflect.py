class Person(object):

    def __init__(self,name = None):
        print("Inside Person's init")
        self.name = "Dinesh"

    def __getattr__(self, item):
        print(" Inside getattr ", item)
        if item == "name":
            print(" Inside if condition ")
            return item


class Animal(object):
    pass


