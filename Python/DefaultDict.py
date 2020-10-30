'''from collections import defaultdict

s = "mississipi"

d = defaultdict(int)

for i in s:
    d[i]+=1

print d


# Custom callable for default dict

def default_value():
    return 0

d = defaultdict(default_value)

print d["one"]
print d["two"]
'''

# Implementation 1 to count the characters in a string --  not very efficient
s = "mississippi"
d = {}
# for i in s:
#     d[i] = 0

for i in s:
    d.setdefault(i,0)
    d[i]+=1

print d

# Implementation 2 to count the characters in a string
def char_frequency(s):
    dict = {}
    for n in s:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))


