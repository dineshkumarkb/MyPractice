from PlayerFactory import PlayerFactory

class PlayerDemo:

    def getMyPlayer(self):

        _player1 = PlayerFactory.getPlayer("IRDETO")
        _player1.play()

        _player2 = PlayerFactory.getPlayer("Nex Player")
        _player2.play()



pd = PlayerDemo()
pd.getMyPlayer()

