class Merge_Sort(object):

    def __init__(self,unsorted = None):

        if unsorted is None:
            raise Exception," List is Empty "
        else:
            self.unsorted = unsorted
            self.sortedarr = []
            self.start_sort(unsorted)


    def start_sort(self,myarray):

        if(len(myarray) < 2):
            return

        else:
            left = []
            right = []
            mid = len(myarray)//2

            for i in myarray[:mid]:
                left.append(i)

            for j in myarray[mid:]:
                right.append(j)

            self.start_sort(left)
            self.start_sort(right)
            self.merge(left,right,myarray)



    def merge(self,left,right,arr):

        i=j=k= 0

        print " arr value is ",arr

        while i < len(left) and j < len(right):
            if(left[i] < right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while(i < len(left)):
            arr[k] = left[i]
            i += 1
            k += 1

        while(j < len(right)):
            arr[k] = right[j]
            j += 1
            k += 1

        print " Sorted arr value is ", arr






if __name__ == "__main__":
    a = [2, 4, 1, 3, 8, 9, 0, -2, -1]
    Merge_Sort(a)