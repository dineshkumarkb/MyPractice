from LoggerFactory import LoggerFactory

class TestLogger:

    def main(self):

        logger =  LoggerFactory.newLogger(LoggerFactory.console)
        if logger.connect():
            logger.log("Test Message 1")
            logger.disconnect()

        else:
            print "Cannot connect to console based logger"

        path = r'D:\File.txt'



        logger = LoggerFactory.newLogger(LoggerFactory.file,path)
        if logger.connect():
            logger.log("Test message for file")
            logger.disconnect()
        else:
            print "Cannot connect to file based logger"



        logger = LoggerFactory.newLogger(LoggerFactory.file)
        if logger.connect():
            logger.log("Test message for file without args")
            logger.disconnect()
        else:
            print "Problem with file"



if __name__ == "__main__":
    t = TestLogger()
    t.main()

