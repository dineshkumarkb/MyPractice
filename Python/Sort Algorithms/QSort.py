class QSort:

    def __init__(self,unsortarray = None):

        if(unsortarray != None):
            if hasattr(unsortarray,"append"):
                print " The argument is a list "
                self.myarray = unsortarray
                low = 0
                high = len(self.myarray) - 1
                self.startSort(low,high)
            else:
                raise TypeError," The passed argument is not a list "

    def startSort(self,low,high):

        i = low
        j = high

        while(i <= j):

            pivot = self.myarray[(low + high)//2]
            print " The pivot is ", pivot

            while(self.myarray[i] < pivot):
                i+=1

            while(self.myarray[j] > pivot):
                j-=1

            if(i <= j):
                self.myarray[i],self.myarray[j] = self.myarray[j], self.myarray[i]
                i+=1
                j-=1
        print " i and j values are ", i , j
        print " low and high values are ", low, high
        print " Full Array is ", self.myarray
        print " Array1 ", self.myarray[low:i]
        print " Array2 ", self.myarray[j:high]

        if(low < j):
            self.startSort(low,j)

        if(i < high):
            self.startSort(i,high)

    def getSortedList(self):

        return self.myarray





if __name__ == "__main__":
    mylist = [30,20,10,40,80,90,100,50,60,70]
    q = QSort(mylist)
    print q.getSortedList()
