import threading, time

class MyThread7(threading.Thread):

    def __init__(self):

        threading.Thread.__init__(self)
        print "Start of main thread"

    def run(self):

        i = 0
        while(i < 10):
            print "Inside run method"
            time.sleep(3)
            i+=1
        print "Terminating child thread"

    def checkmain(self):

        print "Inside Main thread check main method"

    def startmythread(self):

        self.start()

    print "End of main thread"


t = MyThread7()
t.startmythread()