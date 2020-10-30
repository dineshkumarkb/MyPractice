class Node(object):

    def __init__(self, item):
         if(item is not None):
             self.item = item
             self.next = None

    def getNext(self):
        return self.next

    def setNext(self,nextitem):
        self.next = nextitem

    def getCurrentData(self):

        return self.item

    def displayItems(self):

        print " The item objects are ", self.item




