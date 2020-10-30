
"""
class Employee():

    emp_count=0
	  
    def __init__(self, name, sal):
        assert isinstance(name,str)
        self.name=name
        self.sal=sal
        Employee.emp_count+=1
	
    def display_count(self):
        self.dpcount=dpcount
        print "The employees count is:" , self.dpcount
		#print " The total number of employees are:", Employee.emp_count
	
    def display_emp(self):
		print "the emp name", self.name,"Salary", self.sal
	
	
emp1=Employee("25",8000)
emp2=Employee("Ramesh",7000)

emp1.display_emp()

from dis import dis

from selenium.webdriver.remote import webelement



from urlparse import *
#from urlparse import urlsplit

prsd = urlsplit("https://www.facebook.com/photo.php?fbid=955365477842179&set=a.137769162935152.20864.100001062080740&type=1&theater&notif_t=like")

print prsd




d={"Name":"Dinesh","Mobile":9027}
d1={"Loc":"Madurai"}
d.update(d1)
e=("name","mobile")
print str(d)
for i in d:
 print i, d[i]
#a = raw_input("Please enter your name:")
#print a
b=d.fromkeys(e)
print b
s=str(d)
print type(d)
assert isinstance(s,str)
if cmp(d,d1):
 print ("Inside if condition")
#a =int(a)
#assert isinstance(a,str)


#d1={"Name":"Dinesh" ,"No":9027 ,"Name":"Sharath","No":9845}
#print d1["Name"]


l1=["Dinesh","Deepi","Sasi","KTB"]
l2=["Symphony","Nagra","Cisco","Wipro"]
#d1={"Name":"Dinesh","Company":"Symphony"}
for i in range(len(l1)):
  l1.extend(l2.pop())
print l1

from string import Template
s=Template($x need to become an expert in $y)
s.substitute("$x" = "Dinesh","$y" = "Python")



#import xlrd
#import os.path
#ws = xlrd.open_workbook("D:\Sanity Test Reports\Sanity_Test_Report_ExoPlayerSampleapp_1.33_HLS_TS_Android_4.4.2.xlsx")
#print ws.sheet_names()
f= open ("C:\Users\indkumar05\Desktop\Test URLs.txt", "r+")
s= f.read()
m3u8_count=s.count("m3u8")
mp4_count = s.count("mp4")
print f.tell()
#f.write("I am writing this at the end")
print "The number of m3u8s are:", m3u8_count
print "The number of mp4s are:", mp4_count
f.close()
f=open("C:\Users\indkumar05\Desktop\Test URLs.txt", "r+")
f.write("Test URLs written by Python")
f.close()
#print "The number of passed scripts are :", pass_count




f = open ("D:\Python\Dinesh.txt","r+")
s =  f.read()
print s
f.close()
cnt = s.count("Dinesh")
print cnt
if cnt > 0:
  s = s.replace("Dinesh","Conviva")
  cnt1=s.count("Conviva")
else:
  s = s.replace("Conviva","Dinesh")
  cnt1=s.count("Dinesh")
print cnt1
assert cnt1==cnt," Not all strings are replaced"  
f = open ("D:\Python\Dinesh.txt","r+")
f.write(s)


from math import sqrt
s = {}
sqrt = 'print "This is test code"'
exec sqrt in s

import urlparse
from urlparse import urlsplit
user_url =  raw_input("\n Please copy the url you wanna parse and split:\n")
user_url=user_url.strip()
parsed = urlparse.urlparse(user_url)
split = urlsplit(user_url)
print "\n", parsed
print "\n" ,split
if user_url.endswith(".m3u8"):
  print "HLS"
l = list(parsed)
#print l
if "https" in l:
  print "\n This is a secured website"
elif "http" in l:
  print "\n This is not a secured website"
  


def fib(n):  
  for i in range(n):
     l.append(l[-2]+l[-1])
  return l 
  
l = [0,1]
n = input("Enter the range till which u wanna print the fibonacci")
fib (n)
print l
print len(l)


with open("D:\Python\Dinesh.txt","r+") as f:
    s = f.read()
    s= s.strip()
    l = []
    l.append(s)
    print l[0]

import json
import pprint
#from pprint import pprint
with open("C:\Users\indkumar05\Desktop\orange_configs_sdk.json","r+") as contents:
  jscontents = contents.read()
  #pprint.pprint(jscontents)
  #pprint(jscontents)
  print jscontents.count("contentSrc")
  move = jscontents.index("contentSrc")
  contents.seek(move)
  print contents.tell()
  #print jscontents
  
  
  #def enablepreroll(self):
    #    prerolltoggle = MyProject()
    #    prerolltoggle.myjsonchange()
        	
    #def engateway(self):
    #    wronggateway = MyProject()
    #    wronggateway.gatewaychange()
	#togglegateway = MyProject()
	
	 def readjson(self): 
        # Open the json file and read it
        json_open = open("C:\Users\indkumar05\Desktop\orange_configs_sdk.json","r+")
        json_read = json_open.read()    
		
    def writejson(self):
        fo = open("C:\Users\indkumar05\Desktop\orange_configs_sdk.json","r+")
        fo.write()  
		
		#print dir(MyProject)
        
        #s = os.path.join("C:/", "Users","Dinesh","Desktop","orange_configs_sdk.json")
        s = os.path.join("C:/", "Users","indkumar05","Desktop","orange_configs_sdk.json")
        #d = os.path.join("G:/","test","orange_configs_sdk.json")
        d = os.path.join("\mnt","sdcard")


json_open = open("C:\Users\indkumar05\Desktop\orange_configs_sdk.json","r+")
json_read = json_open.read()
l = json_read.split("adType",3)
pos = json_read.find("http")
json_open.seek(pos)
print json_open.tell()
json_read = json_open.readline()
json_read = json_read.split(",")
print json_read[0]
print json_read
if ".m3u8" in str(json_read):
    print "HLS"
else:
    print "HLS not found"
print json_open.tell()

#http://straightedgelinux.com/blog/python/json.html
#http://stackoverflow.com/questions/20199126/reading-a-json-file-using-python


import random
import os
l = []
for i in range(0,100):
  l.append(random.randrange(1,100))
  
print l
#os.getlogin()
print dir(os)



import smtplib

s = smtplib.SMTP("mail.corp.conviva.com")
s.sendmail("dkumar@conviva.com","dkumar@conviva.com","Hi, Test message from Python")
print "Sent Email"


try:

  s = raw_input("Please enter a string:")
  n = input("Please enter a number:")
  print "This is your name:  %s" % s
  print "This is your num:   %d" % n

except (TypeError,NameError),e:
  print "This is a stupid exception"
  print "\n", e


class MyName:

     def __init__(self,name = "Dinesh",age = 28,prof = "Python"):
     
         self.name = name
         self.age = age
         self.prof = prof
         self.d = {}
         
     def setkey(self,name):
     
        if name:        
           self.d.setdefault(name)
        else:
           try:
             self.d.setdefault(self.name)
             self.d.setdefault(self.age)
             self.d.setdefault(self.prof)
           except (TypeError,NameError), e:
             print "You have encountered an error", e            
            
     def getkey(self):
         print self.d.items()
         
         
#m = MyName()
#m.setkey(None)
#m.getkey()
          
class MyName1(MyName):

     def __init__(self):
        
        MyName.__init__(self)     
     
     def getonlykeys(self):
     
         print self.d.keys()
         
     def getonlyvalues(self):
     
         print self.d.values()
          
m1 = MyName1()
m1.setkey("Dinesh")
print m1.age
print m1.prof
m1.setkey("Deepi")
m1.getkey()
m1.getonlykeys()
m1.getonlyvalues()


import random

print "The random integers are: " + str(random.randint(10,9999))


import subprocess
from subprocess import PIPE,Popen

cmd = "ipconfig"

p = Popen(cmd,stderr = PIPE,stdin = PIPE,stdout = PIPE)
subprocess.Popen(cmd)
a = p.communicate()
l = []
a = str(a)
print a


s = "alkjshdjhasjkfhskdjfkjsdhfkjsdhjgkhdfkghkdjfhDineshkajsdhjihsadfhsikdhfksdhgkhfdskg"

def mygen(s):

    for i in s:    
        yield i
        
for i in mygen(s):
    print i
    


s = "alkjshdjhasjkfhskdjfkjsdhfkjsdhjgkhdfkghkdjfhDineshkajsdhjihsadfhsikdhfksdhgkhfdskg"

mystr =  raw_input("Please enter the string you wanna check:")

if mystr in s:
    
    try:    
       loc = s.find(mystr)
       l = len(mystr)
       print s[loc:(loc+l)]       
    
    except IndexError:
        print "Error"


class calc:

     def __init__(self,a,b):     
         self.a = a
         self.b = b
         
     def myadd(self):     
         return self.a + self.b
         
     def mysub(self):     
         if self.a > self.b:
            return self.a - self.b
         elif self.b > self.a:
            return self.b - self.a
            
     def mymul(self):     
         return self.a * self.b
         
     def mydiv(self):     
         return int(self.a/self.b)

a = input("Please enter first number") 
b = input("Please enter second number")
c = calc(a,b)
print c.mydiv()




class MyTest:

    #def __init__(self):    
        
        
        
    def myprint(self,name):
    
        self.name = name    
        print "My name is %s" % self.name
        
        
    def main(self):
    
        n =  raw_input("Please enter your name")
        p = raw_input("Do you want me to print your name?")
        d = MyTest()
        if ((p == "y") or (p =="yes")):        
           d.myprint(n)           
        else:
           return
        
        
        
c = MyTest()
if __name__ ==  "__main__":
     c.main()
           
        


d = range(1,11) + "Jack King Queen".split()
c = "Hearts clubs diamond spades".split()
l = [('%s of %s') %(l1,l2) for l1 in d for l2 in c]
print l

#print zip(l1,l2)




import shelve

s = shelve.open("D:\Python\mydb.dat")
s["Name"] = "Dinesh"
s["Age"] = 28
s["Phone"] = 9972689027

print s.keys()



import socket


s = socket.socket()
print s
myhost = socket.gethostname()
port = 1345

s.connect((myhost,port))


print s.recv(1024)


import requests

class MyLogger:


    def __init__(self):

        self.myurl = "http://touchstone.conviva.com"
        self.mylogin = "dkumar@conviva.com"
        self.mypass = "Pa55w0rd"

    def myLogin(self):

        s = requests.Session()
        self.mydata = {"username":self.mylogin,"password":self.mypass}
        r = s.post(self.myurl,self.mydata)
        mypage = s.get(self.myurl)
        print mypage.content



m = MyLogger()
m.myLogin()


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import requests
from urllib import urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
#driver = webdriver.Firefox()
driver.get("http://touchstone.conviva.com")

mywait = ui.WebDriverWait(driver,5)

#myuserinput = raw_input("Please enter your username:")
#mypassinput = raw_input("Please enter your password:")

myemail = driver.find_element_by_id("loginBox")
myemail.send_keys("dkumar@conviva.com")

mypass = driver.find_element_by_id("passwordBox")
mypass.send_keys("Pa55w0rd")

mylogin = driver.find_element_by_id("loginButton")
mylogin.send_keys(Keys.RETURN)

mylpconfig = driver.find_element_by_id("ui-id-4")
mylpconfig.send_keys(Keys.RETURN)

myselecttouchstone = driver.find_element_by_id("startRemoteWithServiceUrlBtn")
myselecttouchstone.send_keys(Keys.RETURN)

WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CLASS_NAME,"sourceTable")))

#for row in driver.find_elements_by_class_name("sourceTable"):
    #print row.find_elements()
mycount = 1 # Xpath count starts from 1

WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CLASS_NAME,"lastSeenActive")))
#WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"//*[@id='clientsDiv']/table/tbody/tr/td[3]/text()")))
mycount = 1
#for row in driver.find_elements_by_css_selector("#clientsDiv > table > tbody > tr.lastSeenActive"):
for row in driver.find_elements_by_xpath("//*[@id='clientsDiv']/table/tbody/tr/td[4]/div"):
    mytest = row.text
    print mytest
    #cell =  row.find_elements_by_tag_name("td")[3]
    #myrowtext = row.find_element_by_xpath("//*[@id='clientsDiv']/table/tbody/tr/td[3]")
    #print cell.txt
    #s = cell.txt
    #print mycount
    myxpath = "//*[@id='clientsDiv']/table/tbody/tr[{}]/td[7]/input".format(mycount)
    #print myxpath
    if mytest == "test video":
       #mybutton = row.find_element_by_xpath("//*[@id='clientsDiv']/table/tbody/tr/td[7]/input")
       mybutton = row.find_element_by_xpath(myxpath)
       mybutton.click()
       break
    mycount+=1







for row in driver.find_elements_by_css_selector("#clientsDiv > table > tbody > tr.lastSeenActive"):
    #print row
    cell =  row.find_elements_by_tag_name("td")[3]
    print cell.text
    print mycount
    if cell.text == "Unfinished Business":
        mybutton = row.find_element_by_xpath("//*[@id='clientsDiv']/table/tbody/tr['+mycount+']/td[7]/input")
        mybutton.click()
    mycount+=1


#mytesturl = driver.current_url
#print mytesturl

#clientsDiv > table > tbody > tr:nth-child(7) > td:nth-child(7) > input
#clientsDiv > table > tbody > tr:nth-child(7) > td:nth-child(7) > input
//*[@id="clientsDiv"]/table/tbody/tr[7]/td[4]/div

#myselectdevice = driver.find_element_by_id("mainDiv")
#myhtmltable = driver.find_element_by_class_name("lastSeenNew")
#myhtmltable  = driver.find_element_by_xpath(".//*[@id='clientsDiv']/table/tbody")
#myhtmltable = driver.find_element_by_css_selector(".lastSeenNew>td")
#print myhtmltable

myurlcontent = urlopen("C:\Users\indkumar05\Desktop\Touchstone Certifier - Select Devices.html")

soup = BeautifulSoup(myurlcontent)

print soup

table = soup.find(attrs={"class":"sourceTable"})
print table

#myelements = driver.find_element_by_class_name("sourceTable")
#print myelements

#s =  requests.Session()

//*[@id="clientsDiv"]/table
//*[@id="clientsDiv"]/table
//*[@id="clientsDiv"]/table/thead
//*[@id="clientsDiv"]/table

//*[@id="clientsDiv"]/table/tbody
.//*[@id='clientsDiv']/table/tbody

#clientsDiv > table




import json

f = open(r'D:\\orange_configs_sdk.json')
s = f.read()
j  = json.loads(s)
for i in j:
    print i
#print json.JSONDecoder(j).decode("contentSrc")


n = input('> ')
m = n-1

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:   # top or left edge
            print 1+i+j,
        elif i == m or j == m: # right or bottom edge
            print 2*n-1-i-j ,
        else:                  # inside
            print ' ',
    print

for i in range(5):
    for j in range(5):
        if (i == 0 or j == 0):
            print j+1+i,
        elif (i == 4 or j == 4):
            print 10-1-i-j,
        else:
            print " ",

    print


for i in range(5):
    for j in range(5):
        if j == 0 or i == 0:
            print j+1+i,
        elif j == 5-1 or i == 5-1:
            print 2*5-j-1-i,
        else:
            print " ",

n = 5
for i in range(n):
    #for j in range(n):
        print " " * (n-1-i) + "*" * (2 * i + 1)

class Response:

    response_data = {'url': '','status': '','data': '' }

    def set_message(self, key, value):

        try:

            self.response_data[key] = value
            print Response.response_data
            print self.response_data
        except Exception as e:
            raise Exception(e)

    def getdict(self):

        return Response.response_data

response = Response()
response.set_message('success', "success")

a = None
print type(a)


m = "String"
l = len(m)
print m[:l]
print m[-1:-7:-1]
print m[-l:]
print m[::-1]



def mynumber(n):

    k = 5

    for i in range(1,n,2):
        print " " * k + str(n) * i
        k-=1
        n-=1


mynumber(8)


def mynumber(n):

    k = 5
    n1 = n
    for i in range(1,n):
        print " " * i + str(n) * n1
        n1-=2
        n-=1


mynumber(8)





n = 5
for i in range(n):

    print " " * (n+1) + "*" * (i*2 + 1)
    n-=1


import Tkinter
import time

x = 5


top = Tkinter.Tk()


def updateText():

    mytext.set("Changed")
    mytext.set("Changed again")
    mytext.set("Changed 3rd time")


mytext = Tkinter.StringVar()

button = Tkinter.Button(top, textvariable = mytext, command = updateText)
mytext.set("Initial")



button.pack()

top.mainloop()



# ctx = None
#
# class Test:
#
#     def getCtx(self):
#         global ctx
#         ctx.testme = True
#
#
#
# t = Test()
# t.getCtx()

# a = "dinesh"
# b = "dinesh"
#
# c = a
#
# print a == b
# print a is b
# print a == c
# print c is a
#
# a= "kumar"
# print c is a
# print c
# print a
# l = [1,2,3,4,5]
#
# def func1(l):
#     for i in range(len(l)):
#         l[i] = l[i] + 1
#
#     print l
#
# func1(l)
# print l


#! python3
# PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6','blog':'VmALvQyKAxiVH5G8v0lif1MLZF3sdt','luggage': '12345'}
# import sys, pyperclip
# if len(sys.argv) <2:
#     print('Usage: python pw.py[account] -  copy account password')
#     sys.exit()
#
# account = sys.argv[1]  #first command line arg is the account name
#
# if account in PASSWORDS:
#     pyperclip.copy(PASSWORDS[account])
#     print ('Password for ' + account + ' copied to clipboard.')
# else:
#     print ('There is no account named ' + account)
#     print ('There is no account named ' + account)


# mylist1 = [{"name" : "dinesh" , "age" : 25},{"name" : "Ramesh"},{"key3" : "value3"}]
# mylist2 = [{"name" : "dinesh", "age" : 23},{"name" : "testname"},{"key3" : "value3"},{"key4" : "value4"}]
# newlist = []
#
# for elements1 in mylist1:
#      for elements2 in mylist2:
#          if(elements1 == elements2):
#              print elements1.items()

# from collections import defaultdict
#
# data = [(0, 0, {'product_id': 6, 'qty': 1.0}),
#         (0, 0, {'product_id': 8, 'qty': 1.0}),
#         (0, 0, {'product_id': 7, 'qty': 2.0}),
#         (0, 0, {'product_id': 6, 'qty': 1.0}),
#         (0, 0, {'product_id': 8, 'qty': 1.0}),
#         (0, 0, {'product_id': 7, 'qty': 2.0})]
#
# newdict = defaultdict(float)
# l = []
# for x,y,mydict in data:
#     myid = mydict['product_id']
#     myvalue = mydict['qty']
#     newdict.setdefault(myid,0)
#     newdict[myid] += myvalue
#
# print newdict

# mydict = {'Sex':['Male','Male','Female','Female','Male'],
#     'Height': [100,200,150,80,90],
#     'Weight': [20,60,40,30,30]}
#
# print zip(mydict['Sex'],mydict['Height'],mydict['Weight'])
#
# for x,y,z in zip(mydict['Sex'], mydict['Height'],mydict['Weight']):
#     print x,y,z


# mydict = {"name" : ["Dinesh","Ramesh","Ganesh","Suresh"],
#           "age"  : [25,26,27,28],
#           "dept" : ["ece","ece","eee","mech"]
#           }
#
# print [(a,b,c) for a in mydict['name'] for b in mydict['age'] for c in mydict['dept']]

# print zip(mydict["name"],mydict["age"],mydict["dept"])
#
# for x,y,z in zip(mydict["name"],mydict["age"],mydict["dept"]):

#     print x,y,z

# a = [1,2,3,4]
# b = a
# a.append(5)
# print id(a), id(b) , a, b

# result = []
#
#
# def remove_duplicates(s):
#     count = 0
#     if(len(s) > 0):
#         for i in s:
#             if i not in result:
#                 result.append(i)
#             else:
#                 count+=1
#     return count
#
#
#
# c = remove_duplicates("abc")
# print ("".join(result),c)

# l = range(10)
# l1 = l[:]
#
# print l
# for i in l[:]:
#     l.remove(i)
#
# print l

#
# import MySQLdb
# import csv
# db=MySQLdb.connect(user='root',passwd='toor',
#                         host='127.0.0.1',db='data')
# cursor=db.cursor()
# csv_data=csv.reader(file('C:\Users\indkumar05\Desktop\File1.txt'))
# for row in csv_data:
#         sql = "insert into `kelembapan` (`id`,`Tanggal`,`Tipe_sensor`,`Value`,`Ket`) values(%s,%s,%s,%s,%s);"
#         cursor.execute(sql,row)
# db.commit()
# cursor.close()
# print "The Data has been inputted"

# import math
# import argparse
# parser = argparse.ArgumentParser(description='This will compute the power of given input number')
# parser.add_argument('-p', '--power', type=int, help='Server name', required=True)
# args = parser.parse_args()
# print args


# import requests
#
# myurl = r'http://maps.googleapis.com/maps/api/geocode/json'
# add = r'21A/12,Ramasamy Naidu Street, Old Mahalipatti Road, Madurai-625001'
# parameters = {'address': add,"sensor" : False}
#
# r = requests.get(myurl)
# a = r.json()
# print a


# import httplib
# import urllib
# import json
#
# base = r'maps/api/geocode/json'
# path = '{}?address={}&sensor=false'.format(base,urllib.quote_plus(r'207 N. Defiance St, Archbold, OH'))
# conn = httplib.HTTPConnection("maps.google.com")
# conn.request("GET",path)
# rawreply = conn.getresponse().read()
# print " Raw reply is : ", rawreply
# reply = json.loads(rawreply.decode('utf-8'))
# print " Reply is ", reply


# import socket
# import urllib
#
# request_text =
#
# GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1\r\n
# HOST: maps.google.com:80\r\n
# User-Agent: Dinesh
# Connection: close\r\n
# \r\n
#
#
# address = "207 N. Defiance St, Archbold, OH"
# sock = socket.socket()
# sock.connect(("maps.google.com",80))
# request = request_text.format(urllib.quote_plus(address))
# sock.sendall(request.encode("ascii"))
# raw_reply = "b"
# while True:
#     more = sock.recv(4096)
#     if not more:
#         break;
#     raw_reply+= more
# print(raw_reply.decode('utf-8'))


# import json
# from pprint import pprint
# s1 = open(r'/Users/dkumar/Desktop/orange_configs_sdk.json').read()
# #s = json.loads(s1)
# s = json.load(open(r'/Users/dkumar/Desktop/orange_configs_sdk.json'))
# pprint (s[0]['ad_protocol'])
# # for d in s:
# #     print d['autoCreateSession']

# a = 'HelloWorld'
# s = a.rstrip("He")
# print s

# l = [0,1]
#
# for i in range(5):
#     l.append(l[-2] + l[-1])
#
#
#
# print l



# def triangle(n):
#
#     tot = 0
#
#     # for i in range(n):
#     #     tot += n
#     #     n-=1
#     # print tot
#
#     while(n >= 1):
#         #print " n = ", n
#         tot += n
#         n-=1
#         #print " tot inside loop = ", tot
#
#     print tot
#
#
# triangle(10)


# a1 = [10,23,38,45,54]
#
# i = 0
#
# print len(a1)
# while(i <= len(a1)):
#     print a1[i]
#     i+=1

# def Merge(left, right, A):
#     i = j = k = 0
#
#     while (i < len(left) and j < len(right)):
#         if (left[i] < right[j]):
#             A[k] = left[i]
#             i += 1
#
#         else:
#             A[k] = right[j]
#             j += 1
#
#         k += 1
#
#     while (i < len(left)):
#         A[k] = left[i]
#         i += 1
#         k += 1
#
#     while (j < len(right)):
#         A[k] = right[j]
#         j += 1
#         k += 1
#
#
# def MergeSort(A):
#     left = []
#     right = []
#     n = len(A)
#     if (n < 2):
#         return
#     mid = n / 2
#     for i in range(mid):
#         left.append(A[i])
#     for i in range(mid, n):
#         right.append(A[i])
#
#     MergeSort(left)
#     MergeSort(right)
#     Merge(left, right, A)
#
#
# A = [2, 4, 1, 3, 8, 9, 0, -2, -1]  # given unsorted array
# MergeSort(A)
# print A


# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#     if (year % 4 == 0):
#         if (year % 100 == 0):
#             if(year%400 == 0):
#                 leap = True
#         else:
#             leap = True
#
#     return leap
#
# year = int(raw_input("Year:"))
# print is_leap(year)
#
# i = 2
# j = 2
# k = 2
# n = 2

# print [[i,j,k] for i in range(i+1) for j in range(j+1) for k in range(k+1) if((i+j+k) != n)]
#
# arr = []
# for i in range(i+1):
#     for j in range(j+1):
#         for k in range(k+1):
#             if((i+j+k) != n):
#                 arr.append([i,j,k])
#
# #print arr

# if __name__ == '__main__':
#     n = int(raw_input())
#     arr = map(int, raw_input().split())
#     #print arr
#     arr_m = set(arr)
#     arr_m.remove(max(arr_m))
#     print arr_m
#     print max(arr_m)

# l = [2,3,5,4,6,6]
#
# mymax = max(l)
# count = 0
#
# while max(l) == mymax:
#     print " The max element now is : ", max(l)
#     l.remove(max(l))
#
# print max(l)


# class CustomException(Exception):
#
#     pass
#
#
# class TestCustomException(object):
#
#     def __init__(self, arg1 = None):
#
#         if(arg1 is None):
#             raise CustomException
#
#
#
#
# TestCustomException()



#
# if __name__ == '__main__':
#     l = []
#     N = int(raw_input())
#
#     for i in range(N):
#         command = raw_input().split()
#         print command
#
#         if command[0] == "insert":
#             l.insert(int(command[1]), int(command[2]))
#         elif command[0] == "remove":
#             l.remove(int(command[1]))
#         elif command[0] == "append":
#             l.append(int(command[1]))
#         elif command[0] == "pop":
#             l.pop()
#         elif command[0] == "sort":
#             l.sort()
#         elif command[0] == "reverse":
#             l.reverse()
#         elif command[0] == "print":
#             print l
#         else:
#             break
#


#Replace all ______ with rjust, ljust or center.

#
#
# thickness = int(raw_input()) #This must be an odd number
# c = 'H'
#
# #Top Cone
# for i in range(thickness):
#     print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)
#
# #Top Pillars
# for i in range(thickness+1):
#     print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)
#
# #Middle Belt
# for i in range((thickness+1)/2):
#     print (c*thickness*5).center(thickness*6)
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)
#
# #Bottom Cone
# for i in range(thickness):
#     print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)


# def capitalize(string):
#
#     slist = []
#     for c in string.split(" "):
#         if c:
#             slist.append(c.capitalize())
#         else:
#             slist.append(c)
#     return " ".join(slist)
#
# if __name__ == '__main__':
#     string = raw_input()
#     capitalized_string = capitalize(string)
#     print capitalized_string
#
# import textwrap
#
# value = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
#
# # Wrap this text.
# wrapper = textwrap.TextWrapper(width=4)
#
# word_list = wrapper.wrap(text=value)
#
# print "\n".join(word_list)



# def test_rec(n):
#     if n < 1:
#         return
#     test_rec(n-1)
#     print n
#
# test_rec(10)



# import os
# import sys
#
# print os.environ.get("PATH")
# print sys.path


# from TimeIt.STime import STime
#
# def test_fun(n):
#
#     STime.start()
#     print STime.get_start_time()
#     sm = 0
#     for i in range(n):
#         for j in range(n):
#             #print i,j
#             sm+=j
#
#
#     STime.stop()
#     print STime.get_stop_time()
#
#     print STime.get_interval()


#test_fun(9000)


# 2018-09-10 20:04:26.338000
# 2018-09-10 20:04:26.371000
# 0:00:00.033000

# l = [1,2,3]
# print l[:]



# x1 = [1,2,3]
# x2 = [4,5,6]
#
#
# x1values = 0
# x2values = 0
# for i,j in zip(x1,x2):
#     x1values += i
#     x2values += j
#
#
# print x1values, x2values



