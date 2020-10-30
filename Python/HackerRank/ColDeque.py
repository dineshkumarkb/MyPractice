from collections import deque
n =  input()
d = deque()
for i in range(n):
    t = raw_input().split()
    f = getattr(d,t[0])
    if len(t) > 1:
        f(t[1])
    else:
        f()


for i in d:
    print i,

