from abc import ABCMeta,abstractmethod

class Logger:

    __metaclass__ = ABCMeta

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def log(self, msg):
        pass



'''class LogTracker(Logger):

    def __init__(self):
        print "This is from LogTracker class"

    def connect(self):
        return "Connected"

    def disconnect(self):
        return "Disconnected"

    def log(self, msg):
        print "The message to be logged is", msg


l = LogTracker()
print l.connect()
print l.disconnect()
l.log("My first python abstract class")'''
