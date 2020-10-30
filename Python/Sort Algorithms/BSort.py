class BubbleSort:

    def __init__(self,mylist):

        assert isinstance(mylist,list)," Please pass a list object "
        self.mylist = mylist
        self.mysort()

    def mysort(self):

        for i in range(len(self.mylist)-1):
            for j in range(len(self.mylist)-i-1):
                if(self.mylist[j] > self.mylist[j+1]):
                    self.mylist[j],self.mylist[j+1] = self.mylist[j+1],self.mylist[j]

        return self.mylist



lest = [20,10,50,90,40,30]
b = BubbleSort(lest)
print b.mysort()