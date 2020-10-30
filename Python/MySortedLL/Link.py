class Link(object):

    def __init__(self,data):
        self.data = data
        self.next = None

    def setNext(self,nnext):
        self.next = nnext

    def getNext(self):
        return self.next

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def printList(self):
        print " The value is ", self.data
