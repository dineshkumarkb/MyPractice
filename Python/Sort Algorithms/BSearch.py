class BinarySearch(object):

    def __init__(self,unsortedarr = None,issorted = False):

        assert isinstance(unsortedarr,list), " The passed argument is not a list "
        self.myarray = unsortedarr

        if(not issorted):
            self.myarray.sort()

    def search(self,item):

        low = 0
        high = len(self.myarray) - 1

        while(True):

            center = (low + high)//2

            if(item == self.myarray[center]):
                print " Item  found at ", self.myarray.index(item)
                break

            elif (low > high):
                print " Item not found "
                break

            elif(item < self.myarray[center]):
                high = center - 1

            elif(item > self.myarray[center]):
                low = center + 1

            else:
                print "Failed"
                break


if __name__ == "__main__":
    mylist = [x for x in xrange(100) if(x%2) == 0]
    b = BinarySearch(mylist,True)
    b.search(98)
