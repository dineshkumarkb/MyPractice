# l = [x for x in xrange(30) if(x % 2 != 0)]
# print l
#
# l1 = [x*2 for x in xrange(10)]
# print l1
#
# mylist = [1,2,3,4,2,4]
#
# l2 = set([x for x in mylist if(mylist.count(x) > 1)])
# print l2
# d = {"key" : "value"}
# import collections
#
# print hash(d["key"])
# print hash("string")
#
# print collections.Counter(mylist)
#
# l3 = [i for i in mylist if(i%10)!=0]
# print l3

# list1 = [1,2,3,4,6]
# list2 = [7,8,9,10,11]
#
# list3 = [(x,y) for x in list1 for y in list2]
# #print list3
#
# def mysplit(s):
#     return s.strip()
# slist = ["Dinesh "," Ganesh "," Ramesh "]
# list4 = [mysplit(x) for x in slist]
# print list4


# flist = [(lambda x: x+2)(x) for x in range(5)]
# print flist

# s = 12345678
#
# lst = [int(i) for i in str(s)]
# #print lst
#
# mylist = []
#
# for i in str(s):
#     mylist.append(int(i))
# #print mylist
#
#
# mylist = [1,2,3,4,5,6,7,8,9,0]
# x = 100
#
# #Desired output tuple(1,x)(2,x)
#
# print [(a,x) for a in mylist]

x = ["1_1",23,"1_2",35,"1_1",20,"1_3",20,"1_2",40]
d = {}
# for i in xrange(len(x)//2):
#     print i, x[(2 * i)]
#     d[x[2 * i]] = x[(2*i)+1]
#


s = "Ant man 2015 HDRIP"

s1 = s.split(" ",3)

print " ".join(s1[0:3])





a = [1,2]
b = [3,4]


for i in a:
    for j in b:
        print (i,j)



