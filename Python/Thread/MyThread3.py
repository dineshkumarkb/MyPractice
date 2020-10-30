import threading,time,random

class MyThread3(threading.Thread):

    balance = 0

    def __init__(self):

        threading.Thread.__init__(self)

        #super(MyThread3, self).__init__()


    def withdraw(self, amount):

        if(amount <= MyThread3.balance):
            try:
                time.sleep(random.randint(1,3))
                MyThread3.balance-=amount
                return True

            except KeyboardInterrupt as KI:
                print "The program has been interrupted", KI

        return False

    def run(self):

        tname = self.getName()
        for i in range(10):
            print " {} withdraws 10$ {} ".format(tname,self.withdraw(10))



if __name__ == "__main__":


    MyThread3.balance = 100
    t1 = MyThread3()

    t1.setName("Hubby")
    t1.start()

    t2 = MyThread3()
    t2.setName("Wife")
    t2.start()






