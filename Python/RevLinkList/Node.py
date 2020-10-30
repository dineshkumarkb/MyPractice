class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next

    def setNext(self,newnext):
        self.next = newnext

    def setData(self,new_data):
        self.data = new_data

    def display(self):
        print self.data
