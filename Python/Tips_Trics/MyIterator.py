class Repeater(object):

    def __init__(self,value):
        self.value = value

    def __iter__(self):
        return RepeatIterator(self)


class RepeatIterator(object):

    def __init__(self, obj):
        self.obj = obj
        self.max = 5
        self.count = 0

    def __next__(self):
        if self.count <= 5:
            self.count += 1
            return self.obj.value

        raise StopIteration



repeater = Repeater("Hello")


for r in repeater:
    print(r)

