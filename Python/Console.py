from Logger import Logger


class Console(Logger):

    def __init__(self, dstName = None):

        self.dstName = dstName

    def connect(self):
        return True

    def disconnect(self):
        return True

    def log(self,msg):
        print "The console logs are : ", msg
        return True



