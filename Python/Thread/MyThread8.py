import threading


class MyThread8(threading.Thread):

    count = 1000

    def __init__(self):

        threading.Thread.__init__(self)

        self.name = self.getName()
        self.threadLock = threading.Lock()

    def run(self):

        #print self.name+  " " + str(self.count)

        while(MyThread8.count > 900):

            self.threadLock.acquire()
            print "Accessed from {} {}".format(self.name, self.printme())
            self.threadLock.release()

    def printme(self):

        MyThread8.count-=10
        return MyThread8.count



t = MyThread8()
t.setName("Dinesh-1")



t1 = MyThread8()
t1.setName("Dinesh-2")
t.start()
t1.start()





