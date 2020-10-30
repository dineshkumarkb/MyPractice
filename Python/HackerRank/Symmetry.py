n =  input()
a = set(map(int,raw_input().split()))
m = input()
b = set(map(int,raw_input().split()))
v1 = a.difference(b)
v2 = b.difference(a)
l = []
for i in v1:
    l.append(i)
for j in v2:
    l.append(j)

for k in sorted(l):
    print k


