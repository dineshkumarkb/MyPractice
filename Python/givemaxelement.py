class RetMax:

    def givememax(self,mylist):

        if hasattr(mylist,"append"):
            for i in range(len(mylist)-1):
                if l[i] > l[i+1]:
                    l[i],l[i+1] = l[i+1],l[i]

            return l[-1]





if __name__ == "__main__":
    r= RetMax()
    l = [i for i in range(100)]
    print r.givememax(l)
