class MergeSort(object):

    def __init__(self,a = None):

        if a is None:
            raise Exception," Array is empty "
        else:
            self.arr = a
            self.start_merge(self.arr)

    def start_merge(self,arr):

        print " The arr value is ", arr
        #print " The low and mid values are {} ".format(arr)

        left = []
        right = []

        if len(arr) < 2:
            return

        else:
            mid = (len(arr))/2
            for i in range(mid):
                left.append(arr[i])
            for j in range(mid,len(arr)):
                right.append(arr[j])
            self.start_merge(left)
            self.start_merge(right)
            self.merge_sort(left,right,arr)


    def merge_sort(self,left,right,arr):

       # print " The low mid high values are {} {} {} ".format(low,mid,high)

        i = 0
        j = 0
        k = 0

        while (i < len(left)) and (j < len(right)):
            if(left[i] < right[j]):
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1

            k+=1

        while(i < len(left)):
            arr[k] = left[i]
            i+=1
            k+=1


        while (j < len(right)):
            arr[k] = right[j]
            j += 1
            k += 1
        print arr





a = [2,4,1,3,8,9,0,-2,-1]
m = MergeSort(a)

