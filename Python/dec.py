'''def myname(name):
    return name

Name = myname
print Name("Dinesh")

def greet(name):
    print locals()
    def get_message():
        print locals()
        return "Hello "

    result = get_message()+ name
    return result

print greet("Dinesh")


def greet:
    return "Hello " +name

def call_func(func):
    other_name = "john"


def inc(n):
    assert isinstance(n,object)
    print "Inside inc"
    return n

@inc
def add(a,b):
    return a+b

print add(1,2)

from functools import wraps

def mydec(f):
    @wraps(f)
    def wrapped(*args,**kwards):
        print "Before Decorated function"
        r = f(*args,**kwards)
        print "After Decorated function"
        return r
    return wrapped

@mydec
def myfunc(myarg):
    print " my func", myarg
    return "return value"

r = myfunc("abcd")
print r

def myaddcheck(f):
    print f
    f1 = f(3,4)
    print f1
    return f

@myaddcheck
def add(a,b):
    print "Inside add"
    return a+b

c = add(1,2)
print c

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
while True:
   c, addr = s.accept()
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.close()

   '''

import socket

class Server1:

    def __init__(self,myhost = None,myport = 12345):

        self.s = socket.socket()
        self.port = myport

        if myhost == None:
            self.host = socket.gethostname()

        else:
            self.host = myhost

        print "The following configuration has been assigned"
        print "The host is ", self.host
        print "The port is ", self.port


    def myserver(self):

        #print "The current host is " , socket.gethostbyname(self.host)
        #print " The current host addr is ", socket.gethostbyaddr(self.host)
        self.s.bind((self.host,self.port))
        self.s.listen(5)
        while True:
            c,address = self.s.accept()
            print "Started Listening  to", address
            c.send("Connected! This is just a test socket program to see if am able to connect")
            print c.recv(1024)


s = Server1()
s.myserver()










