# Below code is my approach which doesnt look elegant
'''
n = input()
l = map(int,raw_input().split())
c = input()
l1 = []
for i in range(c):
    l1.append(raw_input().split())

mysum = 0
for ele in l1:
    if int(ele[0]) in l:
        mysum += (int(ele[1]))
        l.remove(int(ele[0]))

print mysum

'''

# Below is inspired from hackerrank discussions

from collections import Counter

n =  input()
s = Counter(map(int,raw_input().split()))
c = input()
profit = 0

for i in range(c):
    ssize,price = map(int,raw_input().split())
    if s[ssize]:
        profit+=price
        s[ssize]-=1

print profit






