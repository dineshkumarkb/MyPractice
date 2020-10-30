class SelectionSort:

    def __init__(self,mylist):

        if(hasattr(mylist,"append")):
            self.mylist = mylist
        else:
            raise TypeError," Not of type list "

    def start_sort(self):

        for i in range(len(self.mylist)):
            mymin = self.mylist[i]
            for j in range(i+1,len(self.mylist),1):
                if(self.mylist[j] < mymin):
                    mymin = self.mylist[j]
            print " The change in main list ", self.mylist[i], self.mylist.index(mymin)
            pos = self.mylist.index(mymin)
            self.mylist[i], self.mylist[pos]  = self.mylist[pos], self.mylist[i]

            print self.mylist

        return self.mylist



if __name__ == "__main__":
    lest = [20,10,50,90,40,30]
    s = SelectionSort(lest)
    print s.start_sort()
