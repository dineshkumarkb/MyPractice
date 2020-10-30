import random

class Shuffler:

    myrandom = random.Random()

    def __init__(self, mylist):

        if hasattr(mylist,"append"):
            self.list = mylist
            self.length = len(mylist)
        else:
            raise AttributeError

    def main(self):

        for i in range(self.length):
            s = Shuffler.myrandom.randrange(self.length)
            self.list[i], self.list[s] = self.list[s], self.list[i]

        print self.list



s =  Shuffler([1,2,3,4,5,6,7,8,9,10])
s.main()




