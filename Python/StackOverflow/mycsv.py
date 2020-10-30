# import copy
# mylist = [1,2,[3,3],4,5,6,7]
#
# #mylist_1 = mylist[:]
# mylist_1 = copy.deepcopy(mylist)
#
# mylist_1[2][0] = 12
#
# print(mylist_1)
# print(mylist)
#
# new_arr = list(range(0,10))
# print(new_arr)



def _print_name(name):
    print(f"Hi {name} ")

# print_name("Deepika")


def call_me(myfunc, myparam):
    myfunc(myparam)


call_me(print_name,"Deepika")