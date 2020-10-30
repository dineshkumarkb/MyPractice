from SList import SList

class WrapList(object):

    def __init__(self):
        self.first = None

    def is_empty(self):
        return self.first == None

    def ins_sort(self,data):
        slist = SList(data)
        current = self.first
        prev = None

        while(current != None):
            if(data > current.getData()):
                prev = current
                current = current.getNext()
            else:
                break


        if(prev == None):
            self.first = slist
        else:
            prev.setNext(slist)
        slist.setNext(current)

    def display(self):
        current = self.first
        while(current != None):
            current.printAll()
            current = current.getNext()


if __name__ == "__main__":
    wlist = WrapList()
    wlist.ins_sort(23)
    wlist.ins_sort(32)
    wlist.ins_sort(20)
    wlist.ins_sort(19)
    wlist.ins_sort(40)
    wlist.display()










