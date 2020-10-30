class SSort:

    def __init__(self,mylist):

        if(hasattr(mylist,"append")):
            self.mylist = mylist
            print self.start_sort()
        else:
            raise TypeError, "Please pass a list"


    def start_sort(self):

        for i in range(len(self.mylist)):
            #Ensure minimum is set as index value rather than value in the list
            # If list value is set, we have to be cautious while swapping.
            # Swap with the index in the list, rather than the minimum value itself.
            minimum = i
            #Comparison should start from i+1 to ensure we compare the
            #consecutive elemets
            for j in range(i+1,len(self.mylist),1):
                if(self.mylist[j] < self.mylist[minimum]):
                    minimum = j
            self.mylist[i],self.mylist[minimum] = self.mylist[minimum],self.mylist[i]

        return self.mylist


if __name__ == "__main__":
    lest = [20, 10, 50, 90, 40, 30]
    s = SSort(lest)

