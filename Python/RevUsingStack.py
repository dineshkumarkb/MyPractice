from MyStack import MyStack
import sys

class RevString(object):

    def __init__(self, mystring):

        if (mystring != None and (len(mystring) > 0)):
            self.mystring = mystring
            self.mystack = MyStack(len(mystring))
            self.start_reverse()
        else:
            print " Please pass a valid string "
            sys.exit(0)


    def start_reverse(self):
        o = ""
        for s in self.mystring:
            self.mystack.push(s)
        for i in range(self.mystack.get_size()):
            o = o + self.mystack.popout()
        print o

if __name__ == "__main__":

    s = raw_input(" Please enter the string to be reverse : ")
    rs = RevString(s)






