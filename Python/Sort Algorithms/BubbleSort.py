import sys

class BubbleSort:

    def __init__(self,myList):

        self.myList = myList
        if hasattr(self.myList,"append"):
                print " The passed object is a list. Proceeding to sort "
                self.startSort()

        else:
            raise TypeError," The passed object is not of type List "

    def startSort(self):
        for i in xrange(len(self.myList)):
            for j in xrange(len(self.myList)-1):
                if self.myList[j] > self.myList[j+1]:
                    self.myList[j], self.myList[j+1] = self.myList[j+1], self.myList[j]

        print " The sorted list is ", self.myList


l = [876,456,32,1,90,400,45,87,34,1]
d = {}
b = BubbleSort(l)
