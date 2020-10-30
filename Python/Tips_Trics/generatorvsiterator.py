class MyIterator(object):

    def __init__(self,max_count):

        self.max_count = max_count
        self.count = 0


    def __iter__(self):

        self.start = 0
        return self


    def __next__(self):

        if self.start < self.max_count:
            self.count = self.start
            self.start += 1
        else:
            raise StopIteration
        return self.count



m = MyIterator(10)

# for i in m:
#     print(i)



def myiterator(max_count):
    for i in range(max_count):
        yield i

myiterator_obj = myiterator(3)

print(next(myiterator_obj))
print(next(myiterator_obj))
print(next(myiterator_obj))
print()

for i in myiterator(10):
    print(i)
