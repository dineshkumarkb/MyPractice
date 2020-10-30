from Console import Console
from FileMe import FileMe


class LoggerFactory:

    console = 0
    file = 1

    @staticmethod
    def newLogger(dstType, dstName = None):

        if(dstType == LoggerFactory.console):
            c = Console()
            return c

        elif (dstType == LoggerFactory.file):

                f = FileMe(dstName)
                return f




