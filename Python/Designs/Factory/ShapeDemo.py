from ShapeFactory import ShapeFactory

class ShapeDemo:

    def __init__(self):
        pass

    def main(self):

        mycircle = ShapeFactory.createobject("Circle")
        mycircle.draw()

        myrectangle = ShapeFactory.createobject("Rectangle")
        myrectangle.draw()



s = ShapeDemo()
s.main()

