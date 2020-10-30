# l = [1,"a",2,"b",3,"c",4,"d"]
# # d = dict()
# # for i in range(len(l)-1):
# #     d[l[i]] = l[i+1]
# #
# # print(d)
#
# #print(l[::2])
#
# # print({l[i]:l[i+1] for i in range(len(l)-1)})
#
#
# t1 = ("name","age")
# t2 = ("dinesh",33)
#
# print(dict(zip(t1,t2)))
#
# #print(dict(l))
#
# #def get_values():
#
# #l = ["name","address","age","sex"]
# mydict = dict.fromkeys(l)
# print(mydict)
# #print(iter(l))
# # print(dict(zip(l,l)))
# # l1 = iter(l)
# # print(dict.fromkeys(l[::2],next(l1)))
# iter_val = iter(l)
# ele1 = next(iter_val)
# ele2 = next(iter_val)
# print(ele1,ele2)

from string import Template

s = "$user is logged in as $role"
t = Template(s)
new_string = t.safe_substitute(user="Programmer")
print(new_string)


