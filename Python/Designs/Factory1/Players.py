from abc import abstractmethod,ABCMeta

class Players(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def printPlayer(self):
        pass




