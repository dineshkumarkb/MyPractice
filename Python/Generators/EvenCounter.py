class EvenCounter(object):

    def __init__(self,count_value):
        if count_value == 0:
            return
        else:
            self.count = count_value

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        if self.start <= self.count:
            self.start+=2
        else:
            raise StopIteration
        return self.start

    def next(self):
        return self.__next__()


c = EvenCounter(10)


"""Even Counter implemented using generator"""


def even_counter(n):
    start = 2
    while(start <= n):
        yield start
        start+=2

for i in even_counter(10):
    print i
