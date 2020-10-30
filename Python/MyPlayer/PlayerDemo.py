from GenericPlayer import GenericPlayer
from Player import Player
from ExoPlayer import ExoPlayer
from MediaPlayer import MediaPlayer

class PlayerDemo:

    def myMain(self):

        p = Player()
        m = MediaPlayer()
        e = ExoPlayer()
        p.registerListener(m)
        p.registerListener(e)
        p.play()
        p.pause()
        p.stop()
        p.removeAllListeneres()
        p.play()
        p.pause()
        p.stop()


if __name__ == "__main__":
    p = PlayerDemo()
    p.myMain()



