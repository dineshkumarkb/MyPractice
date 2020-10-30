from abc import abstractmethod,ABC

class Player(ABC):

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def seek(self):
        pass

    @abstractmethod
    def getPlayerName(self):
        pass

class PlayerFactory(object):

    def __new__(cls, playerName,*args, **kwargs):

        return super(PlayerFactory, cls).__new__(eval(playerName),*args, **kwargs)


class ExoPlayer():

   def getExoPlayer(self):

       return PlayerFactory(self.__class__.__name__)


class NexStreaming():

    @staticmethod
    def getNexPlayer():

        return PlayerFactory(__class__.__name__)



#print(PlayerFactory())
e = ExoPlayer()
print (e.getExoPlayer())

print (NexStreaming.getNexPlayer())









