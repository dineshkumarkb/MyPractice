class BSort:
    """
    This class is to perform a Bubble sort.
    Bubble sort will compare adjacent elements and swap the elements.
    At the end of first pass, the biggest element will be at the end of the list
    This will be suitable only for smaller arrays
    """

    def __init__(self,mylist):

        self.mylist = mylist

        if  hasattr(mylist,"append"):
           print "Inside if"



    def sortme(self):
        """
        This method has the core logic to perform the bubble sort.
        It will compare adjacent elements and sort them. The number of passes will be more
        if the number of elements in the array is more as we are comparing adj elements.
        For instance, if the array is completely sorted after 2 passes still the loop continues
        which makes it slower and ineffecient for larger arrays
        :return:
        """

        # Iterate through all the elements in the list
        for i in range(len(self.mylist)):
            # Iterate to compare and swap the current and next element till the end of list
            for j in range((len(self.mylist)-1-i)):
                if self.mylist[j] > self.mylist [j + 1]:
                    self.mylist[j],self.mylist[j + 1] = self.mylist[j + 1],self.mylist[j]

        print  self.mylist


if __name__ == "__main__":
    l = [876,456,32,1,90,400,45,87,34,1]
    b =  BSort(l)
    b.sortme()

