from InitLink import InitLink

class LList(object):

    def __init__(self):
        self.first = None

    def insertFirst(self, iid, name):
        init_link = InitLink(iid,name)
        init_link.setNext(self.first)
        self.first = init_link

    def getSize(self):

        current = self.first
        count = 0
        while(current != None):
            count+=1
            current = current.getNext()

        return count

    def search(self,iid):
        current = self.first
        while(current != None):
            if current.getData()[iid] == iid:
                found = True
            else:
                current = current.getNext()

        return found


    def delete(self,iid):
        current = self.first
        prev = None
        while current != None:
            if(current.getData()[0] == iid):
                break
            else:
                prev = current
                current = current.getNext()

        if prev == None:
            self.first = current.getNext()
        else:
            prev.setNext(current.getNext())


    def isEmpty(self):

        return self.first == None

    def getList(self):
        current = self.first
        while(current != None):
            current.displayList()
            current = current.getNext()

if __name__ == "__main__":
    llist = LList()
    llist.insertFirst(1,"Dinesh")
    llist.insertFirst(2,"Kumar")
    llist.insertFirst(3,"TestUser1")
    llist.insertFirst(4,"TestUser2")
    print llist.getSize()
    llist.delete(4)
    llist.getList()






