class ISort(object):

    def __init__(self,unsorted_list):
        if(unsorted_list is None):
            raise Exception, " List object is None "
        else:
            self.unsorted = unsorted_list
            llength = len(self.unsorted)
            self.start_sort(self.unsorted)


    def start_sort(self,myarr):

        if(len(myarr) <= 1):
            return
        for i in range(1,len(myarr),1):
            j = i

            while(j >= 1 and myarr[j] < myarr[j-1]):
                myarr[j],myarr[j-1] = myarr[j-1],myarr[j]
                j-=1

        print myarr


if(__name__ == "__main__"):
    i = ISort([25,12,7,3,2])
