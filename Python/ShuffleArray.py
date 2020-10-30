import random

class ShuffleArray:

    mylist = []


    def __init__(self,mylist):

        self.mylist = mylist
        self.size = len(self.mylist)
        print self.startShuffle()
        self.factoryShuffle()

    def getList(self):

        return self.mylist

    def startShuffle(self):
        for i in range(self.size):
            self.myindex = random.randint(0,self.size-1)
            self.mylist[i], self.mylist[self.myindex] = self.mylist[self.myindex], self.mylist[i]

        return self.mylist

    def factoryShuffle(self):

        self.myFactoryIndex = random.shuffle(self.mylist)
        # for i in range(len(self.size)):
        #     self.mylist[self.myFactoryIndex] = self.mylist[i]

        print "Factory Shuffled List", self.mylist








l = [1,2,3,4,5]
s = ShuffleArray(l)
#print s.getList()