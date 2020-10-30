import socket
import random

class Server(object):

    def __init__(self):

        self.myList = [" Advice 1 ", " Advice 2 ", " Advice 3 "]
        self.host = socket.gethostname()
        self.port = 8888
        s = socket.socket()
        s.bind((self.host,self.port))
        s.listen(10)

        while(True):
            c,addr = s.accept()
            print " The addr value is ", addr
            print " The client value is ", c.recv(1024)
            adv = random.randint(0, len(self.myList) - 1)
            c.send(self.myList[adv])
            c.send("Thanks for connecting")
            c.close()

Server()

