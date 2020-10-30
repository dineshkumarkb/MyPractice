class MergeArrays1:

    def __init__(self):

        self.result = []

    def main(self):

        a = [1,2,3,4,5]
        b = [6,7,8,9,10]
        self.merge(a,b)

    def merge(self,x,y):

        if x == None:
            raise Exception, "x cannot be empty"
        if y == None:
            raise Exception,"y cannot be empty"

        for i in x:
            self.result.append(i)

        for j in y:
            self.result.append(j)

        assert self.containsAll(self.result,x,y)
        print self.result

    def containsAll(self,myarray,c,d):

        '''for i in range(len(c)):
            if(not self.contains(myarray,c[i])):
                return False

        for j in range(len(d)):
            if(not self.contains(myarray,d[i])):
                return False'''

        for i in range(len(c)):
            for ele in myarray:
                if c[i] == ele:
                    return True

        for j in range(len(d)):
            for ele in myarray:
                if d[i] == ele:
                    return True

        return False

    def contains(self,testarray,val):

        for ele in testarray:
            if ele == val:
                return True

        return False


m = MergeArrays1()
m.main()