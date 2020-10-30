class ShSort(object):

    def __init__(self,unsorted_list = None):
        if(unsorted_list is None):
            raise Exception," List cannot be None "
        else:
            self.unsorted = unsorted_list
            self.length_list = len(unsorted_list)
            self.start_sort()


    def start_sort(self):

        """
        This sort basically compares the items in distance rather than adjacent elements
        The distance between elements will be calculated based on Knuth's series.
        Example 3*h + 1 (0th element, 4th element an 8th element)
        :return: None
        """

        #Calculate Knuth's series based on the length of the list
        h = 1
        while(h <= (self.length_list//3)):
            h = (h * 3) + 1
        print " h value is ", h

        # Start sorting the elements
        # Always compare with 0 so that the condition for 1 also should be checked
        while(h > 0):

            print " Inside h > 0 while "
            for i in range(h,self.length_list,1):
                print " The h value inside for is ", h
                temp = self.unsorted[i]
                j = i
                print " Comparing indexes {} and {} ".format(j,j-h)
                #print " Comparing {} and {} ".format(self.unsorted[j-h],self.unsorted[j])
                while(j > (h-1) and self.unsorted[j-h] >= temp):
                    self.unsorted[j] = self.unsorted[j-h]
                    j-=h
                    print " The decremented j value is ",j
                self.unsorted[j] = temp
            h = (h-1)//3

        print self.unsorted






if __name__ == "__main__":
    l = [23,12,17,10,5,30,50,42,35,3]
    s = ShSort(l)