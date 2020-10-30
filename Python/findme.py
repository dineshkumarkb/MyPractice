l = [[1,2,3],[34,21,12],[9,8,70]]


def findme(l, number):

    for myindex, mylist in enumerate(l):
        #print mylist
        if number in mylist:
            #print "Found in the {} index".format(myindex)
            for i,j in enumerate(mylist):
                if number == j:
                    print "The requested element in found in l[{}][{}]".format(myindex,i)



findme(l, 9)

