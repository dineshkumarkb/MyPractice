import threading
import time

exitflag = 0
class MyThread(threading.Thread):

    def __init__(self,mythreadid,name,counter):

        threading.Thread.__init__(self)
        self.mythreadid = mythreadid
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting" + self.name
        print_time(self.name,5,self.counter)
        print "Exiting" + self.name


def print_time(threadname,delay,counter):
    while counter > 1:
        if exitflag:
            threadname.exit()
        time.sleep(delay)
        print "%s %s" %(threadname,time.ctime(time.time()))
        counter-=1


thread1 = MyThread(1,"thread1",10)
thread2 = MyThread(2,"thread2",5)

thread1.start()
thread2.start()


print "Exiting main thread"

