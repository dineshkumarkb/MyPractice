import json

mydict = {}
with open("mytext.txt", "r") as f:
    for line in f:
        mylst = line.rstrip('\n').split(":")
        mydict[mylst[0]] = mylst[1]


print(mydict)


print([int(x) for x in "1-3-6-16-20" if x != "-"])