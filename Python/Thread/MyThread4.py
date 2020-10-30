import threading

class MyThread4:

    def __init__(self, balance):

        self.balance = balance

    def printme(self, name):

        print "This is printed from {} ".format(name)


    def main(self):

        t1 = threading.Thread(target = self.printme, name = "Dinesh", args= ("Dinesh",))
        t2 = threading.Thread(target = self.printme, args = ("Ajitha",))
        print t1.getName()
        print t2.getName()
        t1.start()
        t2.start()



if __name__ == "__main__":

    m =  MyThread4(100)
    m.main()

