from givemaxelement import RetMax

class Retmin(RetMax):

    def givememax(self,mylist):

        if hasattr(mylist,"append"):
            for i in range(1,len(mylist)):
                j = i
                while (j > 0 and mylist[j] < mylist[j - 1]):
                    mylist[j],mylist[j - 1] = mylist[j - 1],mylist[j]
                    j-=1
            return mylist

    def givememin(self,mylist):

        for i in range(len(mylist)):
            minimum = i
            for j in range(i+1,len(mylist)):
                if mylist[minimum] > mylist[j]:
                    minimum = j

            mylist[minimum],mylist[i] = mylist[i],mylist[minimum]
        return mylist

r = Retmin()
l = [87,45,32,1,90,400,45,87,34,1]
print r.givememax(l)
print r.givememin(l)