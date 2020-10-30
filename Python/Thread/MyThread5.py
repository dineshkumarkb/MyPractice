import threading
import time


class MyThread5(threading.Thread):

    mylist = [12,23,34,43,10,15,54]

    def __init__(self):

        threading.Thread.__init__(self)

    def getlength(self):

        try:
            MyThread5.mylist.pop()
        except IndexError as IE:
            print IE

        return len(MyThread5.mylist)

    def run(self):

        lock = threading.Lock()
        name = self.getName()
        lock.acquire()
        for i in range(10):
            print "The length of mylist is accessed by {}  and the length is {}".format(name, self.getlength())
        lock.release()


if __name__ == "__main__":

    t1 =  MyThread5()
    t1.setName("Thread 1")

    t2 = MyThread5()
    t2.setName("Thread 2")

    t1.start()
    t2.start()



