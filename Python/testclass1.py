class One:

    @staticmethod
    def display():
        print " Inside Class One Static method"
        print "DInesh"

    def mydisplay(self):
        print "Dinesh from Instance method"


class Two(One):

    pass

    #@staticmethod
    #def display():
    #    print "Dinesh from class Two Static method"



#Two.display()

t = Two()
o = One()

Two.display()

print dir(t)
print dir(o)