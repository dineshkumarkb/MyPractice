import copy

l1 = [1,2,3]

l2 = copy.deepcopy(l1)
print(id(l1),id(l2))
print(id(l1[0]),id(l2[0]))
l2.append(4)
print(l1,l2)