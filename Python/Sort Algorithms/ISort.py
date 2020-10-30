class ISort:

    def __init__(self, mylist):

        assert isinstance(mylist,list), " Please pass a list object "

        self.mylist = mylist
        self.start_sort()

    def start_sort(self):

        for i in range(len(self.mylist)):

            j = i

            while(j > 0 and (self.mylist[j-1] > self.mylist[j])):

                self.mylist[j],self.mylist[j-1] =  self.mylist[j-1],self.mylist[j]
                j-=1
                print self.mylist



if __name__ == "__main__":
    i = ISort([20, 10, 50, 90, 40, 30])