"""
This is an example to demo an odd counter using our own implementation
This uses __iter__ and __next__
"""

class OddCounter(object):

    def __init__(self,countvalue):
        self.count = countvalue
        self.start = 1

    def __iter__(self):
        print "__iter__ called"
        return self

    def __next__(self):
        print "__next__ called"
        if(self.start <= self.count):
            self.start+=2
        else:
            raise StopIteration
        return self.start

    def next(self):
        return self.__next__()



mycounter = OddCounter(10)


"""
Implementation of odd counters using generators
"""


def odd_counter(n):
    start = 1
    while(start <= n):
        yield start
        start+=2

#print odd_counter(10)


for i in odd_counter(10):
    print i