def calcPow(n):

    num = 1
    for i in range(1,n+1):
        num = num * 2

    print num


calcPow(4)


def calcnPow(n,p):
    num = 1
    for i in range(1,p+1):
        num = num * n

    print num


calcnPow(3,20)
print pow(3,20)

s = "Helloworld"

print s[3:7]
print s[0].capitalize() + s[1:]