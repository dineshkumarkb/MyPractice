class MyRepeater:

    def __init__(self, mylist):
        self.mylist = mylist

    def __iter__(self):
        return MyRepeaterIterate(self)


class MyRepeaterIterate:

    def __init__(self, obj):
        self.obj = obj

    def __next__(self):
        return self.obj.mylist


mr = MyRepeater("Dinesh")

for m in mr:
    print(m)


