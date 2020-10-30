class FibGen(object):

    def __init__(self,count):
        self.count = count

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.start = 1
        return self

    def __next__(self):

        while(self.start <= self.count):
            self.c = self.a + self.b
            self.a,self.b = self.b,self.c
            self.start+=1
            return self.c

        raise StopIteration

    def next(self):
        return self.__next__()


f = FibGen(10)
for i in f:
    print i

"""
Implementation of fibonacci using generators
"""

def fib(n):
    a = 0
    b = 1
    f = 1
    count = 1
    while(count <= n):
        yield f
        f = a + b
        a,b = b,f
        count+=1

for i in fib(10):
    print i







