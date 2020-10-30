def gen_fib(n):
    a = 0
    b = 1
    count = 0
    while(count <= n):
        c = a+b
        yield c
        a = b
        b = c
        count+=1

#print next(gen_fib(10))
for i in gen_fib(10):
    print i

#Above function with Iterator classes

class Gen_Fib(object):

    def __init__(self,n):
        self.n = n

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.count = 0
        return self

    def next(self):
        return self.__next__()

    def __next__(self):

        self.c = self.a + self.b
        if(self.count <= self.n):
            self.a,self.b = self.b,self.c
            self.count+=1
            return self.c
        else:
            raise StopIteration


g = Gen_Fib(10)

for i in g:
    print i
