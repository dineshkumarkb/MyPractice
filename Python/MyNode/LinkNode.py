from Node import Node

class LinkNode(object):

    def __init__(self):
        self.head = None

    def insert(self,ins_item):
        try:
            node = Node(ins_item)
            node.setNext(self.head)
            self.head = node
        except Exception as e:
            print e.args, e.message

    def find(self,find_item):
        try:
            current = self.head
            while(current.getNext() != None):
                if(current.getCurrentData() == find_item):
                    return True
                else:
                    current = current.getNext()
        except Exception as e:
            print e.message

        return False

    def delete(self,del_item):
        current = self.head
        prev = None
        while(current != None):
            if(current.getCurrentData() == del_item):

                break
            else:
                prev = current
                current = current.getNext()

        if(prev == None):
            self.head = current.getNext()
            print self.head.getCurrentData()
        else:
            prev.setNext(current.getNext())



    def printList(self):
        current = self.head
        print current.getCurrentData()
        while(current != None):
            current.displayItems()
            current = current.getNext()



if __name__ == "__main__":
    linknode = LinkNode()
    linknode.insert("User1")
    linknode.insert("User2")
    linknode.insert("User3")
    linknode.delete("User3")
    linknode.printList()




