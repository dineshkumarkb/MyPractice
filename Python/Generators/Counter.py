class Counter(object):


    def __init__(self,count_value):

        self.count = count_value


    def __iter__(self):
        self.start = 0
        return self


    def __next__(self):
        #print "__next__ called "
        if(self.start >= self.count):
            raise StopIteration
        self.start +=1
        return self.start

    def next(self):

       return self.__next__()



c = Counter(10)

for i in c:
    print i


"""

Above code can be implemented using generators as well

"""



def counter(n):
    for i in range(n):
        yield i


for i in counter(10):
    print i