import socket

class Server1:

    def __init__(self):

        self.host = socket.gethostname()
        self.port = 12345
        self.go()

    def go(self):

        s = socket.socket()
        s.bind((self.host,self.port))
        s.listen(5)
        c,addr = s.accept()
        c.send(" Hi from Server1 , Thanks for connecting")
        print c.recv(1024)


s = Server1()
