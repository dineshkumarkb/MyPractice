import socket

class Client1:

    def __init__(self):

        self.host = socket.gethostname()
        self.port = 12345
        self.go()

    def go(self):

        s = socket.socket()
        s.connect((self.host,self.port))
        s.send(" This is a hi message from {} ".format(self.host))
        print s.recv(20000)


c = Client1()