class CustomList1(list):

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if(self.n == 10):
            raise StopIteration
        self.n+=1
        return self.n

    def next(self):
        return self.__next__()

    def __getitem__(self, item):
        if item == 0:
            return
        return super(CustomList1, self).__getitem__(item)






c =  CustomList1()
for i in range(10):
    c.append(i)

print c

for i in range(5):
    print c[i]