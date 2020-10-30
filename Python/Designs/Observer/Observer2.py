from abc import abstractmethod

class Observer2(object):

    def __init__(self):
        self.listeners = []

    def registerListeners(self,listener):
        self.listeners.append(listener)

    def updateAll(self):
        for listener in self.listeners:
            listener.play()
            listener.stop()


class Observable(object):

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Player1(Observable):

    def play(self):
        print " play from Player1 "

    def stop(self):
        print " stop from Player2 "

class Player2(Observable):

    def play(self):
        print " play from Player2 "

    def stop(self):
        print " stop from Player2 "


class MyMain(object):

    def main(self):

        p1 = Player1()
        p2 = Player2()
        o2 = Observer2()
        o2.registerListeners(p1)
        o2.registerListeners(p2)
        o2.updateAll()

if __name__ == "__main__":
    m = MyMain()
    m.main()



