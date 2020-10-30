# Class based iterator which iterates over odd items only

class OddIterator(object):

    def __init__(self, myobj):

        self.myobject =  myobj
        self.max_value = len(myobj)
        self.value = None

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):

        if self.start < self.max_value:
            self.value =  self.myobject[self.start]
            self.start += 2
        else:
            raise  StopIteration

        return self.value


oddonly = OddIterator("Dinesh")

for i in oddonly:
    print(i)

# Generator implementation of above function

def odd_only(myobj):

    max_value = len(myobj)
    start = 0

    while start < max_value:
        value = myobj[start]
        start += 2
        yield value
    raise StopIteration


gen_odd = odd_only("Hello")

for i in gen_odd:
    print(i)


# Generator expression of  above implementation
myobj = "Hello"
my_gen = (x for x in myobj)
for i in my_gen:
    print(i)

