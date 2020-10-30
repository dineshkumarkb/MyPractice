Data = [
    {'name': "John",
     'age': 10},

    {'name': "John",
     'age': 11},

    {'name': "John",
     'age': 12},

    {'name': "Paul",
     'age': 13},

    {'role': "Paul",
     'age': 14},

    {'role': "Paul",
     'age': 15},
]

john = []
paul = []
for data in Data:
    if data.get("name") == "John":
        john.append(data.get("age"))
    else:
        paul.append(data.get("age"))


print(john)
print(paul)