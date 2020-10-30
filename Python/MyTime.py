import time,Tkinter,tkMessageBox
from Tkinter import *

class MyTime:

    def __init__(self):
    
        self.t = Tkinter.Tk()
        self.t.withdraw()
        
    def mytimecheck(self):
       while True:
            self.my_time = time.asctime().split()
            print self.my_time
            if not (("Sun" in self.my_time[0]) or ("Sat" in self.my_time[0])):
               tkMessageBox.showinfo("Hey Dinesh!!"," Have a great day")
               if ((self.my_time[3] > "16:28:00") and (self.my_time[3] < "17:15:00")):
                   tkMessageBox.showinfo("Hey Dinesh!!","Time to Leave")
            else:
              tkMessageBox.showinfo("Hey Dinesh!!"," Have a great weekend")    
        
        
        
        
m = MyTime()
m.mytimecheck()
        