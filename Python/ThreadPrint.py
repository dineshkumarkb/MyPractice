import threading
import time
import random

class Threadprint(threading.Thread):

    def __init__(self, threadid):
        threading.Thread.__init__(self)
        self.threadid = threadid

    def generateid(self, name):

        for i in xrange(10):
            #print "This is printed from {} with threadid {}".format(name, self.threadid)
            print "The generated id is {} from the thread {}".format(i,name)

    def run(self):

        self.lock = threading.Lock()
        self.lock.acquire()
        #print "Thread is acquired by {} with id {}".format(self.getName(), self.threadid)
        self.generateid(self.getName())
        self.lock.release()



tp = Threadprint(0)
tp.setName("Dinesh")

tp1 = Threadprint(1)
tp1.setName("Kumar")

tp.start()
tp1.start()