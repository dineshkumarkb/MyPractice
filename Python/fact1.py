class Fact1:

    def factorial(self,n):
        num = 1
        for i in range(1,n+1):
            num = num * i

        return num

    def factorial1(self,n):

        if(n == 1 or n== 0):
            return 1
        fact = n * self.factorial1(n-1)
        return fact

    def sum(self,n):

        mysum = 0
        for i in range(1,n+1):
            mysum = mysum + i
        return mysum

f = Fact1()
print f.factorial(10)
print f.factorial1(3)
print f.sum(10)