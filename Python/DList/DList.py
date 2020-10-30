from Node import Node

class DList(object):

    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):

        return self.first is None

    def insertFirst(self,data):
        node = Node(data)
        if(self.isEmpty()):
            self.last = node
        node.setNext(self.first)
        self.first = node

    def insertLast(self,data):
        node = Node(data)
        if(self.isEmpty()):
            self.first = node
        print "self.last is : ", self.last.getData()
        self.last.setNext(node)
        self.last = node


    def deleteFirst(self,data):
        current = self.first
        prev = None
        while current is not None:
            if(data == current.getData()):
                break
            else:
                prev = current
                current = current.getNext()

        if(prev is None):
            self.first = current.getNext()
        else:
            prev.setNext(current.getNext())


    def displayMe(self):

        current = self.first
        #print " self.last value is ", self.last.getData()

        while(current != None):
            current.displayList()
            #print " The value is ", current.getData()
            current = current.getNext()



if __name__ == "__main__":
    dlist = DList()
    dlist.insertFirst("user1")
    dlist.insertFirst("user2")
    #dlist.displayMe()
    dlist.insertLast("user3")
    dlist.displayMe()











