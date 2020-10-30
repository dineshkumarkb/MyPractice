import copy

#Compund Objects
mlist1 = [1,2]
mlist2 = [3,4]
mlist3 = [5,6]

c_list = [mlist1,mlist2,mlist3]

#Shallow copy
copy_list = copy.copy(c_list)
copy_list[0][1] = 10

print c_list,copy_list

#Deep Copy
tlist = [[1,2],[3,4],[5,6]]

d_list = copy.deepcopy(tlist)

d_list[0][1] = 10
d_list[1][0] = 15

print tlist,d_list