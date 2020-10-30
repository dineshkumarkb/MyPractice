class Fact:

    def __init__(self):
        pass

    def factorial(self,n):

        num = 1

        if (n == 0):
            return 1

        while(n >= 1):
            num = n * num
            n-=1
        return num

    def sum(self,n):
        mysum = (n * (n + 1))/2

        return mysum


f = Fact()
print f.factorial(10)
print f.sum(10)

