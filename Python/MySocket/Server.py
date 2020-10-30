import socket

class Server:

    def __init__(self):

        self.go()

    def go(self):

        s = socket.socket()
        s.bind((socket.gethostname(),7777))
        s.listen(5)
        while(True):
            c,addr = s.accept()
            c.send(" Thanks for connecting ")
            c.send(" Thanks again ")
            print c.recv(1024)
            c.close()


Server()
