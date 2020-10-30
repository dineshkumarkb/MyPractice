class LinkedList:


    def __init__(self,start = None,end = None):
        self.mylist = [11,22,33,44,55]
        self.start = self.mylist.index(self.mylist[0])
        self.end = self.mylist.index(self.mylist[-1])

    def reset(self):

        self.start = self.mylist.index(self.mylist[0])
        self.end = self.mylist.index(self.mylist[-1])

    def hasNext(self):
        while(self.start <= self.end):
            return True
        return False

    def hasPrevious(self):
        while (self.end >= self.start):
            return True
        return False

    def __iter__(self):

        return self

    def next(self):

        if(self.start <= self.end):

            temp = self.start
            self.start += 1
            return self.mylist[temp]

        else:
            raise StopIteration

    def previous(self):

        if(self.end >= self.start):
            temp = self.end
            self.end-=1
            return self.mylist[temp]

    def getAll(self):

        while(self.hasNext()):
            print self.next(),

        self.reset()


    def getreverse(self):
        while(self.hasPrevious()):
            print self.previous(),

        self.reset()


    def insertme(self, element):
        self.mylist.append(element)
        self.reset()







l = LinkedList()
#l.getAll()
#print " "
#l.getreverse()
l.insertme(66)
l.getAll()






