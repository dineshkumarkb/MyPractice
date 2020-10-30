n = input()
s = set(map(int, raw_input().split()))
c = input()
for i in range(c):
    f = raw_input().split()
    f1 = getattr(s,f[0])
    if(len(f) < 2):
        f1()
    else:
        f1(int(f[1]))

print sum(s)