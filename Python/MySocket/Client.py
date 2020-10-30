import socket



class Client:

    def __init__(self):
        self.host = socket.gethostname()
        self.port = 7777
        self.go()

    def go(self):

        try:
            s = socket.socket()
            s.connect((self.host,self.port))
            s.send(" Hi from {} {}".format(socket.gethostname(), socket.AF_INET))
            print s.recv(10000)
            s.close()

        except Exception as e:
            print e.message


Client()


