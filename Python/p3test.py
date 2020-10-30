list1 = ["john", "kelvin", "harry", "rob", "jenny", "donne", "justin", "sam", "peter", "kitty"]
list2 = ["radha", "mohan", "pankaj", "sikha", "samarth"]

#print [(list1[a],list1[a+1],b) for a in range(len(list1)-1) for b in list2]


newlist = []
for i in range(0,(len(list1)-1),2):
    for j in range(len(list2)):
        newlist.append((list1[i],list1[i+1],list2[j]))


print newlist