def fibgen(n):
    a = 0
    b = 1
    for i in range(n):
        c = a+b
        a, b = b, c
        yield c

#
# print fibgen(10)
# for i in fibgen(10):
#     print i


class FibGen1(object):

    def __init__(self,count):
        self.count = count

    def __iter__(self):
        self.start = 1
        self.a = 0
        self.b = 1
        self.c = 1
        return self

    def __next__(self):
        if(self.start <= self.count):
            self.c = self.a + self.b
            self.a,self.b = self.b,self.c
            self.start+=1
            return self.c
        else:
            raise StopIteration

    def next(self):
        return self.__next__()


f = FibGen1(10)

for i in f:
    print i

