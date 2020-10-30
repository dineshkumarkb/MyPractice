from Players import Players
from Irdeto import Irdeto
from NexPlayer import NexPlayer

class PlayerFactory:

    player1 = "irdeto"
    player2 = "nex player"


    @staticmethod
    def getPlayer(playerType):

        _playerType = playerType.lower()

        if(_playerType == None):
            return None

        elif _playerType == PlayerFactory.player1:
            print _playerType
            return Irdeto()

        elif _playerType == PlayerFactory.player2:
            print _playerType
            return NexPlayer()

