class Car(object):

    def __init__(self,color,type):
        self.color = color
        self.type = type

    def __str__(self):
        return f"{self.__class__.__name__} with {self.color}"


    def __repr__(self):
        # return f"{self.__class__.__name__}("f"{self.color},{self.type})"
        return f"{self.__class__.__name__}({self.color!r},{self.type!r})"


car = Car("Red","Sedan")
print(str(car))
print(repr(car))
print(eval(repr(car)))
#updated_obj = exec(repr(car))
#print(type(updated_obj))