myPlayers = ["VisualOn", "Exo", "Nex"]

def checkPossibility(playername = None):

    if playername in myPlayers:
        def retFunction(mtd):
            print " Inside return function "
            return mtd
    else:
        def retFunction(mtd):
            print " Inside else condition "
            return mtd

    return retFunction

class TestProtocol:


    @checkPossibility("Test")
    def play(self):
        print " Inside play method "

    @checkPossibility("Exo")
    def pause(self):
        print " Inside pause method "

    @checkPossibility("Exo")
    def stop(self):
        print " Inside stop method "



t = TestProtocol()
t.play()
t.pause()
t.stop()