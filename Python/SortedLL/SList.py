class SList(object):

    def __init__(self,data):
        self.next = None
        self.data = data

    def getData(self):
        return self.data

    def setNext(self,next_item):
        self.next = next_item

    def getNext(self):
        return self.next

    def printAll(self):
        print " The data is : ", self.data

