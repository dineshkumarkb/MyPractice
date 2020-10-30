import sys


class SumNum:

    def __init__(self, num = 0):

        if(num != 0):
            self.num = num
        else:
            print 0
            sys.exit(0)

    def findSumLogicFor(self):

        mysum = 0

        for i in range(1,self.num+1):
            mysum = mysum + i
        return mysum

    def findSumLogicWhile(self):

        mysum = 0

        while(self.num >= 0):
            mysum += self.num
            self.num-=1

        return mysum

    def findSumForm(self):

        return (self.num * (self.num + 1)//2)

    # Sum of n natural numbers =  n * (n+1)//2
    # Missing number = n * (n+1)//2 - sum(n)
    def findMissing(self,myrange):

        if(len(myrange) > 0):
            ap = myrange[-1]
            return (ap * (ap + 1)//2) - sum(myrange)



s = SumNum(3)

print s.findSumForm()
print s.findSumLogicFor()
print s.findSumLogicWhile()
print s.findMissing([1,2,3,5,6])