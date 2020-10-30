class Duplicate(object):

    def __init__(self, mylist):

        if(hasattr(mylist,"append")):
            print " The argument is a list.. proceeding further "
            self.mylist = mylist
            self.dupList = []
            self.findDuplicateByLoop()
        else:
            print " Argument should be a list "

    def findDuplicateByLoop(self):

        print len(self.mylist)

        for i in range(len(self.mylist)):
            for j in range(i+1,len(self.mylist)):
                if(self.mylist[i] == self.mylist[j]):
                    self.dupList.append(self.mylist[i])


        print self.dupList





l = [1,2,2,4,4,5,6,7,8,9,10,5]
d = Duplicate(l)