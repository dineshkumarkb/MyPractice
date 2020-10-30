import threading

class Mythread1(threading.Thread):

    def __init__(self, classname):

        threading.Thread.__init__(self)

        self.call_class = self.getObject(classname)

    def run(self):

        self.call_class.calc()

    def getObject(self, classname):

        myobject =  classname()
        return myobject

class MyName1:

    def __init__(self):

        self.count = 0

    def getName(self):

        pass

    def calc(self):

        for i in range(1,10,1):
            print " From Class MyName1 ", i
            print "\n"

class MyName2:


    def __init__(self):

        self.count = 0

    def getName(self):
        pass

    def calc(self):
        for i in range(10, 20, 1):
            print " From Class MyName2 " , i
            print "\n"






t1 = Mythread1(MyName1)
t2 = Mythread1(MyName2)

t1.start()
t2.start()