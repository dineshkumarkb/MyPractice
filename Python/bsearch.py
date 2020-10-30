class BSearch:

    def __init__(self,mylist):

        self.mylist = mylist

    def searchme(self,element):

        start = 0
        end = len(self.mylist)

        while start <= end:
            print "start = ", start
            print "End = ", end
            mid = (start + end)//2
            print "Mid = ", mid
            if element == self.mylist[mid]:
                print "Inside if"
                return True
            elif element > self.mylist[mid]:
                start = mid+1
            elif element < self.mylist[mid]:
                end = mid - 1
            else:
                print "Element not found"
                break



l = [25,34,45,55,67,99,135,150,178,200]
l.sort()
print l
b = BSearch(l)
print b.searchme(2000)


