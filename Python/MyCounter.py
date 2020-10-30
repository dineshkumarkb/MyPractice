class MyCounter:

    def __init__(self, start, end):

        self.start = start
        self.end = end

    def __iter__(self):

        return self

    def next(self):

        if(self.start <= self.end):

            temp = self.start
            self.start+=1
            return temp

        else:
            raise StopIteration


m = MyCounter(0,10)

for i in m:
    print i
