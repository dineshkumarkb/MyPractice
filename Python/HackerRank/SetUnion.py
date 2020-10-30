n1 = int(raw_input())
e = set(map(int,raw_input().split()))
n2 = int(raw_input())
f = set(map(int,raw_input().split()))


print len(e.union(f))

