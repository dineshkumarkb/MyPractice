class MergeArrays:

    def __init__(self):

        self.result = []

    def main(self):

        a = [1,2,3,4,5]
        b = [1,5,6,7,8,9]
        for i in range(len(a) + len(b)):
            self.result.append(0)
        self.result = self.merge(a,b)
        print self.result

    def merge(self,x,y):

        if x == None:
            raise Exception , "x is Empty"

        if y == None:
            raise Exception, "y is Empty"

        assert isinstance(x,list), "x should be an integer array"
        assert isinstance(y,list),"y should be an integer array"

        for i in range(len(x)):
            self.result[i] = x[i]

        for j in range(len(y)):
            self.result[len(x)+j] = y[j]

        assert self.containsAll(self.result,x,y)

        return self.result

    def containsAll(self,myresult,c,d):

        for i in range(len(c)):
            if(not self.contains(myresult,c[i])):
                return False

        for j in d:
            if(not self.contains(myresult,j)):
                return False

        return True

    def contains(self,urresult,val):

        for ele in urresult:
            if ele ==  val:
                return True

        return False


m =  MergeArrays()
m.main()