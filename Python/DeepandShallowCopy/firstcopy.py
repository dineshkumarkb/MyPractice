import copy

l1 = [[1,2],2,3,4,5]

#l2 = copy.copy(l1)
l2 = copy.deepcopy(l1)

# https://stackoverflow.com/questions/17246693/what-is-the-difference-between-shallow-copy-deepcopy-and-normal-assignment-oper/17246744#17246744
# https://stackabuse.com/deep-vs-shallow-copies-in-python/
# https://stackoverflow.com/questions/17246693/what-is-the-difference-between-shallow-copy-deepcopy-and-normal-assignment-oper/17246744#17246744
print(l1, l2)
print(id(l1), id(l2))
print(id(l1[0]), id(l2[0]))
print(id(l1[1]), id(l2[1]))
print(id(l1[0][0]), id(l2[0][0]))
l1[0][0] = 2
print(id(l1[0][0]), id(l2[0][0]))
print(l1, l2)
l1[0][0] = 2
print(l1, l2)
#print(id(l1[0][0]), id(l2[0][0]))
