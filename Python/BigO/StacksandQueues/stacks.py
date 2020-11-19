class Stack(object):
    """
    This class has a push, pop and peek method.
    peek should return the min value from the stack
    The time complexities of all 3 should be O(1)
    """

    def __init__(self):
        self.stack_ = list()
        self.least = 0
        self.diff = 0
        self.prev_diff = 0

    def push(self, data):

        if not self.stack_:
            self.least = data
            self.stack_.append(data)
        else:
            print(f" data: {data}")
            print(f" min: {self.least}")
            self.stack_.append(data)
            if data < self.least:
                self.least = data

    def pop(self):
        popped_val = self.stack_.pop(-1)
        self.least = self.least - popped_val
        print(f"New least: {self.least}")
        return popped_val


    def peek(self):
        print(f" The min:{self.least}")
        return self.least

    def display_stack(self):
        print(self.stack_)


s = Stack()
s.push(20)
s.push(10)
s.push(30)
s.push(45)
s.push(5)
print(s.peek())
s.display_stack()
s.pop()
s.display_stack()
print(s.peek())
