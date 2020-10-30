import socket

class MyClient:

    def __init__(self):
        self.host = socket.gethostname()
        self.port = 8889
        self.s = socket.socket()

    def myconnect(self):
        self.s.connect((self.host,self.port))
        print "Connected to", self.s.getpeername()
        self.s.send("Hi! I would like to connect to you")
        print self.s.recv(2048)
        self.s.close()



c = MyClient()
c.myconnect()