class Player(object):

    def __init__(self):
        self.listeners = []

    def registerListener(self, genericPlayer):
        self.listeners.append(genericPlayer)

    def removeAllListeneres(self):
        self.listeners[:] = []
        return self.listeners

    def notifyPlayAllListeners(self):
        for listeners in self.listeners:
            listeners.play()

    def notifyPauseAllListeners(self):
        for listeners in self.listeners:
            listeners.pause()

    def notifyStopAllListeners(self):
        for listeners in self.listeners:
            listeners.stop()

    def play(self):
        self.notifyPlayAllListeners()

    def pause(self):
        self.notifyPauseAllListeners()

    def stop(self):
        self.notifyStopAllListeners()


