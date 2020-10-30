class Counter(object):

    def __init__(self,count_val):
        self.count_val = count_val

    def __iter__(self):
        self.start = -1
        return self

    def __next__(self):
        self.start += 2
        if(self.start <= self.count_val):
            return self.start
        else:
            raise StopIteration



    def next(self):
        return self.__next__()


if __name__ == "__main__":
    c = Counter(20)
    for i in c:
        print i
