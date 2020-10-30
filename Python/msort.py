def msort(l):

    if len(l) > 1:

        mid = len(l)//2
        leftside = l[:mid]
        rightside = l[mid:]

        msort(leftside)
        msort(rightside)

        #print "leftside after recursion = " ,leftside
        #print "rightside after recursion = ", rightside

        i = 0
        j = 0
        k = 0

        while i < len(leftside) and j < len(rightside):

            print "leftside[i] = ", leftside[i]
            print "rightside[j] = ",rightside[j]

            if leftside[i] < rightside[j]:
                l[k] = leftside[i]
                i+=1
            else:
                l[k] = rightside[j]
                j+=1
            k+=1

            print "l[k] = ", l[k]

        while i < len(leftside):
            l[k] = leftside[i]
            i+=1
            k+=1

        while j < len(rightside):
            l[k] = rightside[j]
            j+=1
            k+=1


l = [54,26,93,17,77,31,44,55,20]
msort(l)
print l