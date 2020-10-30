# for i in range(1,10,2):
#     print(i)


class CustomIterator(object):

    def __init__(self, step_value, start_value, stop_value):
        self.step = step_value
        self.start = start_value
        self.stop = stop_value
        self.new_start = self.start

    def __iter__(self):
        return self

    def __next__(self):
        self.start = self.new_start
        if self.new_start <= self.stop:
            self.new_start = self.start + self.step
        else:
            raise StopIteration
        print(f" The self.start and new start values is {self.start},{self.new_start}")
        return self.start


c = CustomIterator(step_value=2, start_value=1, stop_value=10)

for i in c:
    print(i)