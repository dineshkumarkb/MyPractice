class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None


    def setNext(self,next_item):
        self.next = next_item

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

    def displayList(self):

        print " The item is : ", self.data
