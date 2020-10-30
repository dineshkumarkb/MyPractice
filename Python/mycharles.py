'''import optparse

def myoptparse():

    parseme = optparse.OptionParser("This is test program for option parser")

    help = "This will set the name of the author"
    parseme.add_option("--name", type = "str" , help = help)

    help = "This will set the number of bytes "
    parseme.add_option("--bytes", type = "int" , help = help)

    options, args = parseme.parse_args()

    print "The options are ",  (options.bytes, options.name)
    print "The args are ", args




myoptparse()

'''

import socket

s =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 8889
s.bind((host,port))
s.listen(10)
path = r'D:\GITRepository\devicesfringe\bcexohlsvod.txt'

with open(path) as f:
    s1 = f.read()

try:
    while True:
        client, addr = s.accept()
        print client.recv(1024)
        client.send("Welcome")


    s.close()
    #s.send(s1)

except KeyboardInterrupt as e:
    print "Exiting", e

