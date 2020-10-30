import threading,time

class ThreadStop(threading.Thread):

    balance = 100

    def __init__(self):
        threading.Thread.__init__(self)
        self.t = threading.Lock()


    def withdraw(self, amount):

        if(amount <= ThreadStop.balance):
            ThreadStop.balance-=amount
            time.sleep(2)
            return True
        return False

    def run(self):

        name = self.getName()
        self.t.acquire()
        for i in range(10):
            print "{} has withdrawn 10$ {}".format(name, self.withdraw(10))
        self.t.release()


ts = ThreadStop()
ts.setName("Dinesh")

ts1 = ThreadStop()
ts1.setName("Aarrti")

ts.start()
ts1.start()





