class Person(object):

    def __init__(self):
        self.name = "Dinesh"
        self.loc = "Bangalore"


p = Person()

g = getattr(p,"name")
print(g)