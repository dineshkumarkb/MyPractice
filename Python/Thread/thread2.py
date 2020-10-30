'''import threading
import time


class MyThread2(threading.Thread):

    def __init__(self, threadid, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadid
        self.name = name
        self.counter = counter

    def run(self):

        print "Starting the thread " + self.name
        threadLock.acquire()
        print_time(self.name, 5, self.counter)
        threadLock.release()


def print_time(name,delay,counter)
    while counter:
        time.sleep(10)


class Test(object):

    def printme(self):
        print "This is just a print"


t = Test()
t.printme()



class ProxyManager(object):

    _myvariable = None

    def __init__(self):
        ProxyManager._myvariable = self
        pass

    @staticmethod
    def testme():
        print "Inside static method"
        if not ProxyManager._myvariable:
            ProxyManager()
        print ProxyManager._myvariable

ProxyManager.testme()

'''

import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("google.com",80))
#s.bind(('localhost', 80))
ip = s.getsockname()
print ip[0]