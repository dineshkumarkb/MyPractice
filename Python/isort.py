'''from bsort import BSort

class ISort(BSort):

    def __init__(self,mylist):
        BSort.__init__(self,None)
        self.mylist = mylist


    def sortme(self):
        """
        This method has the core logic to perform an insertion
        sort
        :return:
        """

        for i in range(1,len(self.mylist)):
            j = i
            while j > 0 and self.mylist[j] < self.mylist[j-1]:
                self.mylist[j],self.mylist[j-1] = self.mylist[j-1],self.mylist[j]
                j-=1

        print self.mylist



if __name__ == "__main__":
    l = [87,45,32,1,90,400,45,87,34,1]
    i = ISort(l)
    i.sortme()

'''


l = [87,45,32,1,90,400,45,87,34,1]

def sortme(l):

    for i in range(1,len(l)):
        j = i
        while (j > 0 and l[j] < l[j - 1]):
            l[j],l[j-1] = l[j-1], l[j]
            j-=1

    print l

sortme(l)