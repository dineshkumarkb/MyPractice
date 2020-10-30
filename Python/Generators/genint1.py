def mycounter(n):
    start = 1
    while(start <= n):
        yield start
        start += 2




g = mycounter(20)

for i in g:
    print i