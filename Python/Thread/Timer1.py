from twisted.internet import task
from twisted.internet import reactor

#timeout = 60.0 # Sixty seconds

def doWork():
    #do work here
    print "do work"

def method2():
    print " Inside method 2"

l = task.LoopingCall(doWork)
l.start(1.0) # call every sixty seconds
reactor.run()
method2()