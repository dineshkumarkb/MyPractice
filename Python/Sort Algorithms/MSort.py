class MSort(object):

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

        mid = len(myarr)//2
        left = myarr[:mid]
        right = myarr[mid:]
        self.start_sort(left)
        self.start_sort(right)
        self.merge(myarr,left,right)


    def merge(self,myarr,left,right):
        i = 0
        j = 0
        k = 0

        while(i < len(left) and j < len(right)):
            if(left[i] < right[j]):
                myarr[k] = left[i]
                i+=1
            else:
                myarr[k] = right[j]
                j+=1
            k+=1

        while(i < len(left)):
            myarr[k] = left[i]
            i+=1
            k+=1

        while(j < len(right)):
            myarr[k] = right[j]
            j+=1
            k+=1

        print self.unsorted


if(__name__ == "__main__"):
    m = MSort([25,12,5,13,7])
