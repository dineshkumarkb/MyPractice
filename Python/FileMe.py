from Logger import Logger

class FileMe(Logger):

    def __init__(self, dstName):

        self.dstName = dstName

    def connect(self):
        if self.dstName == None:
            return  False
        print "Opening file", self.dstName
        return True

    def disconnect(self):
        if self.dstName == None:
            return False
        print "Closing File", self.dstName
        return True

    def log(self, msg):
        if self.dstName == None:
            return False
        print "Logging", msg
        return True



