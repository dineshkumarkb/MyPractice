def sum_num(n):
    start = 1
    while(start <= n):
        yield  (start*(start+1))/2
        start+=1

for i in sum_num(10):
    print i