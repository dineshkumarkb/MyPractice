import copy 

s1 = "dinesh"
s2 = copy.deepcopy(s1)

n1 = 2
n2 = copy.deepcopy(n1)

print(id(s1), id(s2))
print(id(n1), id(n2))
