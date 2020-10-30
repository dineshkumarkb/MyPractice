"""
DO NOT DELETE THE PRINT STATEMENTS FOR THIS PROGRAM.
INTENDED TO UNDERSTAND THE RECURSION
"""
class Merge_Sort(object):

    def __init__(self,unsorted_arr):
        arr = unsorted_arr
        self.start_sort(arr)

    def start_sort(self,myarr):
        print "Starting sort with array : ", myarr
        if(len(myarr) < 2):
            print " myarr len is < 2 returning ",myarr
            return

        low = 0
        high = len(myarr)

        mid = (low + high)//2

        left = myarr[:mid]
        right = myarr[mid:]

        self.start_sort(left)
        print " Calling right array sort "
        self.start_sort(right)
        print myarr
        self.merge(myarr,left,right)

    def merge(self,myarr,left,right):

        i=j=k=0
        print " myarr values are ",myarr
        print " Comparing arrays {} and {} ",left,right

        while(i < len(left) and j < len(right)):



            if(left[i] <= right[j]):
                print " Before Altering myarr value with left ", myarr[k]
                myarr[k] = left[i]
                print " After Altering myarr value with left ",myarr[k]
                i += 1

            else:
                print " Before Altering myarr value with left ", myarr[k]
                myarr[k] = right[j]
                print " After Altering myarr value with right ", myarr[k]
                j+=1

            k+=1


        while(i < len(left)):
            myarr[k] =left[i]
            k+=1
            i+=1

        while(j < len(right)):
            myarr[k] = right[j]
            k+=1
            j+=1


        print myarr








m = Merge_Sort([30,20,10,40,80,90,100,50,60,70])