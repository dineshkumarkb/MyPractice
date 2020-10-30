from Circle import Circle
from Rectangle import Rectangle

class ShapeFactory:


    def __init__(self,myshape):

        self.shape = myshape
        self.createobject(self.shape)

    @staticmethod
    def createobject(shape):

        if shape == "Circle":
            c = Circle()
            return c

        elif shape == "Rectangle":
            r = Rectangle()
            return r

        else:
            return None
