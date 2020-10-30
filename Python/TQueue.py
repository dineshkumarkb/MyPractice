class MyQueue(object):

    def __init__(self, size = None):

            self.que = []
            self.front = 0
            self.rear = 0
            if size is not None:
                self.size = size
            else:
                self.size = 5

    def insert(self,item):
        if((not self.is_full()) and (item > 0)):
            print " Inserting {} at {} ".format(item,self.rear)
            self.que.insert(self.rear,item)
            self.rear+=1
        else:
            raise Exception(" Error Inserting item.Either your queue is full or item is invalid ")


    def remove(self):
        if(not self.is_empty()):
            return self.que.pop(self.front)


    def is_full(self):
        if(len(self.que) == self.size):
            return True
        return False

    def is_empty(self):
        if(self.size == 0):
            return True
        return False

    def peek(self):
        return self.que[0]

    def test_queue(self):
        print self.que



if __name__ == "__main__":
    q = MyQueue()
    q.insert(10)
    q.insert(20)
    q.insert(30)
    q.insert(40)
    q.insert(50)
    q.remove()
    q.remove()
    q.test_queue()
