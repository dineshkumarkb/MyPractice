import threading

class MyThread6(threading.Thread):


    def __init__(self):

        threading.Thread.__init__(self)


    def run(self):
        i = 0
        while(i < 20):
            print "The name of the thread is " + self.getName()
            i+=1



m = MyThread6()
m.start()

m1 = MyThread6()
m1.start()

