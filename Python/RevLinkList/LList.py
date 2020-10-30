from Node import Node

class LList(object):

    def __init__(self):
        self.first = None

    def insert_first(self,data):
        node = Node(data)
        node.setNext(self.first)
        self.first = node

    def print_fwd(self):
        current =  self.first
        while(current is not None):
            current.display()
            current = current.getNext()
        self.print_rev(self.first)

    def print_rev(self,current):
        if(current.getNext() == None):
            return
        else:
            self.print_rev(current.getNext())
            try:
                print current.getData()
            except AttributeError:
                pass






if __name__ == "__main__":
    mylist = LList()
    mylist.insert_first(25)
    mylist.insert_first(15)
    mylist.print_fwd()
    #mylist.print_rev()
