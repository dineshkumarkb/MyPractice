n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
count = 0
for i in range(n):
    for j in range(n-1):
        if(a[j] > a[j+1]):
            count+=1
            a[j],a[j+1] = a[j+1],a[j]

print "Array is sorted in {} swaps.".format(count)
print "First Element: {}".format(a[0])
print "Last Element: {}".format(a[-1])
