import pprint

class InitLink(object):

    def __init__(self, iid = None, name = None):

        if(id != None and name != None):
            self.iid = iid
            self.name = name
            self.next = None

    def getData(self):

        return self.iid,self.name

    def setData(self,iid,name):
        self.iid = iid
        self.name = name

    def setNext(self,nnext):
        self.next = nnext

    def getNext(self):
        return self.next

    def displayList(self):
        print(" The id and names are : {} , {} ").format(self.iid,self.name)

