# lst = ["notebook1", "notebook2"]
#
# restricted_lst = [".,-,"]
#
# def validate_notebook(name):
#
#     if name not in lst and len(name) < 20 and name[0] not in restricted_lst:
#         create_notebook(name)
#     else:
#         raise ValueError
#
#
#
# def create_notbook(name):
#     pass

emp_dict = {"123": "name6", "456": "name4"}

def value_func(v):
    print(v)
    return v.values()

# print(sorted(emp_dict, key=value_func(emp_dict)))

#print(sorted(emp_dict, key=emp_dict))

def sort_my_dict(d):

    names_list = list()
    keys_list = list()
    sort_lst = list(d.values())
    sort_lst.sort()
    print(sort_lst)
    for i in sort_lst:
        for k,v in emp_dict.items():
            #print(f" Comparing values {v} and {i} with key {k}")
            if v == i:
                print(k,v)

    # for v in d.values(): #o(n)
    # #
    # #     names_list.append(v)
    # #
    # # names_list.sort() #o(n log n)

    sorted_dict = dict()

    # for n in names_list:
    #     key_for_value = d
    #     sorted_dict[key_for_value] = n
    #
    # print(sorted_dict)


sort_my_dict(emp_dict)

