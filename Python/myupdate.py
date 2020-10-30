import re
import Tkinter
import tkMessageBox

class MyEdit:

     def __init__(self):
        
        self.f = open("C:\Users\indkumar05\Desktop\orange_configs_sdk - Copy.json","r+")
        self.mystring = self.f.read()
        
     def myprint(self):     
        """ This is to print the contents of the file"""
        print self.mystring
        
     def myreadcontent(self):
        #self.mypattern = r'"contentSrc": "http:.+[\.m3u8\.Manifest]"'
        self.mypattern = r'"contentSrc": "http:.+[\.m3u8]"'
        #r = re.findall(self.mypattern,self.mystring)
        #print r
        #
        #print self.mystring
        if re.search(self.mypattern,self.mystring):
           print "The string is found"
           self.mystring = re.sub(self.mypattern,r'"contentSrc": "http://vevoplaylist-live.hls.adaptive.level3.net/vevo/ch1/appleman.m3u8"',self.mystring)
           tkMessageBox.showinfo("Success","HLS LIVE URL HAS BEEN UPDATED")
           print self.mystring
        else:        
           print "String not found"
           
     def main(self):
        self.d = MyEdit()
        self.t = Tkinter.Tk()
        hls_live = Tkinter.Button(self.t,text = "SET HLS LIVE",command = self.d.myreadcontent)
        hls_live.pack()
        self.t.mainloop()
         
        
e = MyEdit()
#e.myprint()
#e.myreadcontent()
if __name__ == "__main__":
    e.main()
         
         