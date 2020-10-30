from Link import Link

class SortList(object):

    def __init__(self):
        self.head = None


    def insertSort(self,idata):

        link = Link(idata)
        current = self.head
        prev = None

        while(current != None):
            if(idata > current.getData()):
                prev = current
                current = current.getNext()
            else:
                break

        if(prev is None):
            self.head = link

        else:
            prev.setNext(link)
        link.setNext(current)


    def deleteItem(self, item):
        if(self.head is None):
            raise Exception," List is empty "
        current = self.head
        prev = None

        while(current != None):
            if(current.getData() == item):
                prev.setNext(current.getNext())
                print " The item removed is ", current.getData()
                break

            current = current.getNext()

    def displayList(self):
        current = self.head
        while(current != None):
            current.printList()
            current = current.getNext()


if __name__ == "__main__":
    s = SortList()
    s.insertSort(10)
    s.insertSort(30)
    s.insertSort(20)
    s.insertSort(5)
    s.displayList()

