import operator

numbers = [1,2,3,4,5]
# print(operator.itemgetter(1)(numbers))

mydict = {"a":1,
          "b":2,
          "d":4,
          "c":3}

dict_items = mydict.items()
sort_values = sorted(dict_items,key=operator.itemgetter(1))
#print(sort_values)


"""
The below example illustrates using lambda function in key value of sort
"""

test_dict = {
    "key3":[1,5,3],
    "key1":[4,2,9],
    "key2":[7,8,6]
}

test_dict_items = test_dict.items()
#print(f" The sorted items in test_dict are {sorted(test_dict_items)}")

# Sort by first element in value
#print(f" The sort by first element in value is {sorted(test_dict_items, key= lambda x: x[1][0])} ")

# Sort by second element in value
#print(f" The sort by second element in value is {sorted(test_dict_items, key= lambda x: x[1][1])} ")

# Sort by third element in value
#print(f" The sort by third element in values is {sorted(test_dict_items, key=lambda x: x[1][2])}")


"""
The below example illustrates using lambda and dict in key value of srt
"""

item_dict = {
    "id2":{"name":"dinesh","age":52},
    "id1":{"name":"kumar","age":54},
    "id3":{"name":"aji","age":45}
}

item_dict_items = item_dict.items()

print(f" The sorted items in item_dict are {sorted(item_dict_items)}")

# Sort by name in item_dict
print(f" The sorted items by name are {sorted(item_dict_items, key= lambda x: x[1]['name'])}")

# Sort by age in item_dict
print(f" The sorted items by name are {sorted(item_dict_items, key= lambda x: x[1]['age'])}")