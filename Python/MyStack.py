class MyStack(object):

    def __init__(self, size = None):

        self.mystack = []
        self.top = None
        if size is not None:
            self.size = size
        else:
            self.size = len(self.mystack)

    def push(self, element):
        if(self.isFull()):
            raise " Stack Full Error "
        else:
            self.mystack.append(element)
            self.top = self.mystack[-1]


    def popout(self):
        if(self.top == -1):
            raise " Stack Empty Error "
        return self.mystack.pop(-1)


    def get_size(self):

        return self.size

    def isFull(self):

        return len(self.mystack) == 50

    def isEmpty(self):

        return self.top == -1

    def getStack(self):

        return self.mystack


if __name__ == "__main__":
    ms = MyStack()
    ms.push(10)
    ms.push(20)
    print ms.getStack()
    ms.popout()
    print ms.getStack()