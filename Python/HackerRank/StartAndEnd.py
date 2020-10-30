import re



s = raw_input()
k = raw_input()
print s ,k
m = re.finditer(k,s)
for match in m :
    print match