import copy

l1 = ["name","address","empid"]
# shallow copy
l2 = copy.deepcopy(l1)
print(id(l1),id(l2))
print(id(l1[0]), id(l2[0]))
