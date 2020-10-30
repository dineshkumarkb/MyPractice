"""
import sys,time

try:

   s = sys.stdin.read()
   print s
   #time.sleep(5)
      
except: KeyboardInterrupt

finally:
   f = open("D:\Python\Midrollcrash.txt","r+")
   f.truncate()
   f.write(s)
   print "Entered Finally"
   


f = open("D:\Python\Midrollcrash.txt","r+")
while True:
       c = f.read(1)
       print c
       if not c:
          break    
          


f = open("D:\Python\Midrollcrash.txt","r+")
s = f.read()
s = s.split()
print s
"""
import re
f = open("D:\Python\Midrollcrash.txt","r+")
s = f.read()
mypat = r'This.+e'
l = re.findall(mypat,s)
print l
