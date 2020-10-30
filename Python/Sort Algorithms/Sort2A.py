class Sort2Array(object):

    def __init__(self,sa1 = None,sa2 = None):

        if((sa1 is None) or (sa2 is None)):
            raise Exception," One of the arrays is empty"
        else:
            self.array1 = sa1
            self.array2 = sa2
            l1 = len(sa1)-1
            l2 = len(sa2)-1
            self.temp = []
            self.mergeme(self.array1,self.array2,l1,l2)

    def mergeme(self,a1,a2,l1,l2):

        i,j = 0,0


        while((i <= l1) and (j <= l2)):
            if(a1[i] < a2[j]):
                self.temp.append(a1[i])
                i+=1

            else:
                self.temp.append(a2[j])
                j+=1

        while(i <= l1):
            self.temp.append(a1[i])
            i+=1

        while(j <= l2):
            self.temp.append(a2[j])
            j+=1

        print self.temp



if __name__ == "__main__":
    a1 = [10,23,38,45,54]
    a2 = [59,61,67,78,89]
    s = Sort2Array(a1,a2)