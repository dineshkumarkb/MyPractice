import threading,time

class MyThread2(threading.Thread):

    def __init__(self, count):

        threading.Thread.__init__(self)
        self.count = count

    def run(self):

        print "{} initiated".format(self.getName())
        try:
            time.sleep(40)
        except KeyboardInterrupt:
            pass

        print "{} thread is dying".format(self.getName())


t = MyThread2(0)
t.setName("Dinesh")
t.start()
print "Main thread has started"
time.sleep(10)
print "Waiting for the worker thread to complete"
t.join()
print "Main thread is dying"

