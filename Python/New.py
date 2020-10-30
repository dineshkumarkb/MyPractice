import Tkinter
from Tkinter import *
from tkFileDialog import askopenfilename
import thread


class Test1:
  
     def __init__(self,url):
         self.url = url
         
     def sturl(self):
         #self.myurl = myurl
         print self.url
         
class Test2:       
     
    def mythread(self,t):
       print "start"
       self.t.mainloop()
       print "end"
       
    def mybrowse(self):
        self.t = Tkinter.Tk()
        self.t.wm_title("JSON")
        myurl = askopenfilename()
        b = Button(self.t,text = "Browse",command = myurl)
        #url = askopenfilename()
        b.pack()
        #print myurl
        thread.start_new_thread(self.mythread, (self.t,))        
        return myurl
        
 
        

t2 = Test2()
t1 = Test1(t2.mybrowse())
t1.sturl()
while 1:

     print
