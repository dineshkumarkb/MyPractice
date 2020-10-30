'''def triangle(i,j = 0):

    if i == 0:
        return 0
    else:
        print (" " * (i + 1) + "*" * (j*2 + 1))
        triangle(i-1,j+1)

triangle(5)

'''

def tri(n):
    j = 0
    for i in range(n):
        print " " * (n + 1) + "*" * (j*2+1)
        n-=1
        j+=1

tri(5)

n = 5
for i in range(n):
        print " " * (n-1-i) + "*" * (2 * i + 1)