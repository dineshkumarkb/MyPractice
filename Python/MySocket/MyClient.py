import socket

class Client(object):

    def __init__(self):

        s = socket.socket()
        self.host = socket.gethostname()
        self.port =  8888
        s.connect((self.host,self.port))
        s.send(" I am a client {} {} " .format(self.host,self.port))
        print s.recv(1024)
        s.close()


c = Client()