"""
class printname():
 def__init__(self,a,b):
  self.a=a
  self.b=b
  
 def multiplication(self,a,b)   
   return a*b


class MyWorld:

     def __init__(self,name = None,location = None,job = None):
     
         self.name = name
         self.location = location
         self.job = job
         print self.name
         
     def myname(self):
         
         print "The entered name is", self.name
         
     def mylocation(self,location):
         self.location = location
         print "The entered name is", self.location
         
         
     def myjob(self,job):
         self.job = job
         print "The entered job is", self.job
         
m = MyWorld("Dinesh")
m.myname()
m.mylocation("Madurai")
m.myjob("Engineer")
#m.myname()
#m.mylocation()
#m.myjob()


import wx 

class MyUI:

    def __init__(self):
    
       self.app = wx.App()
       self.myframe = wx.Frame(None, title = "My Text Editor", size = (200,200))
       self.mypanel = wx.Panel(self.myframe)
       self.mybutton = wx.Button(self.mypanel,label = "Open",pos = (150,5))
       self.text = wx.TextCtrl(self.mypanel)
       self.textarea = wx.TextCtrl(self.mypanel,pos = (25,20),style = wx.TE_MULTILINE | wx.HSCROLL)
       
       self.vbox = wx.BoxSizer(wx.HORIZONTAL)
       self.vbox.Add(self.text,proportion = 1,flag = wx.EXPAND)
       self.vbox.Add(self.mypanel,proportion = 2)
       #self.vbox.SetSizer()
       
       self.myframe.Show()
       self.app.MainLoop()
    
       
       
m = MyUI()


import pprint
from subprocess import PIPE
import subprocess,re

cmd = "ipconfig"

p = subprocess.Popen(cmd,stdout = PIPE)
a = p.communicate()
s = r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
r = re.findall(s,str(a))
print r
if re.search(s,str(a)):
    print "Network found"
else:
    print "No Network"

import urlparse

myurl = "http://vevoplaylist-live.hss.adaptive.level3.net/livefeed/vevo/ch1.isml/Manifest"
myurl1 = "http://iis7test.entriq.net/Clr/Big_Buck_Bunny.ism/Manifest"

purl = urlparse.urlparse(myurl)
print purl.port


import socket

s = socket.socket()

myhost = socket.gethostname()
port = 1345

s.bind((myhost,port))

s.listen(10)

while True:

     c,addr = s.accept()
     c.send("Thanks for connecting")
     print addr
     c.close()


mycount = 4
s = "//*[@id='clientsDiv']/table/tbody/tr[{}]/td[7]/input".format(mycount)
print s


import time

t = time.asctime()
print str(t)


s1 = "Dinesh"
s2 = 2
print "The variables are {} {}".format(s1,s2)


class MyTest:

    #def mydict(self,mykey):
    #    return self.d[mykey]

    def __getitem__(self, item):
        self.d = {"Name":"Dinesh","Company":"Symphony"}
        return self.d[item]

    def __setitem__(self, key, value):
        self.d[key]= value
        return self.d


m = MyTest()
print m["Name"]
print m["Company"]
m["Loc"] = "Bangalore"
print m.d
print dir(m)




import wx
a = wx.App()
f = wx.Frame(None)
#b = wx.Button(f,label = "Dinesh")
fd = wx.FileDialog()
f.Show()
a.MainLoop()



x = 42
y = x
x+=1

print x
print y



x = [1,2,3]
y = x
x[0]=4
print x
print y


import re
date = "2016-02-25"
time = "10:14:22+0000"

s = r'date = 2016-02-25 time = 10:14:22+0000'

mypattern = r'^date = {0,4}\d-{0,2}\d-{0,2}\d\stime'

print re.search(mypattern,s)




l = [{'name': 'asc'}, {'user_id': 'desc'}]

for query in l:
    if (query.has_key('dinesh')):
        print "Key Found"
    else:
        print "Key Error"




import subprocess
from subprocess import PIPE
cmd = r'ROBOCOPY {} {} {}'.format('D:\\TF1','D:\\TF2','license.xml')
p = subprocess.Popen(cmd,stderr=PIPE,stdout=PIPE)
a = p.communicate()
for i in a:
    print i


def test(init):

    #return  {str(i):init[:] for i in range(0,5)}
    #d = {"0":[],"1":[],"2":[]}
    return d


a = test([])
print "Original : ", a
print type(a)

print a["1"].append("test")
print "Modified : ", a




def fibo(n):

    l = [0,1]
    [l.append(l[-2] + l[-1]) for x in range(n)]
    return l


print fibo(10)





def testme():


    return {str(i):i for i in range(5)}


print testme()




def testme(l = None):

    return [x for x in range(5)]



print testme()



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


b = webdriver.Firefox()
b.get("http://pastebin.com/112g1Gje")
b.find_element_by_class_name("header_icons hi_messages")
"""
# from collections import defaultdict
#
#
# class Bond:
#
#     def __init__(self):
#         pass
#
#
# d ={"key1" : None, "key2" : None, "key3" : None,"key4" : None}
#
#
# defaultdict(dict)
#
# for keys in d:
#     d[keys] = Bond()
#
#
# print (d)
#
# #print (finaldict)
#
# # for keys in d.keys():
# #     d1.setdefault(keys,Bond())
# #
# # print (d1)


#print eval(repr(g)) == g

#print type(eval(o))

#

# import datetime
#
# print(datetime.datetime(2019,7,22,16,22).timestamp())

#import botocore.vendored.requests as requests


# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# import json
#
# d = {"body":"testvalues"}
# if type(d) == dict:
#     print(" It is dict ")
# print(type(d))
# print(json.loads(d))


# import boto3
#
# sm = boto3.client('sagemaker')
#
# print(sm)
#
# response = sm.create_presigned_notebook_instance_url(NotebookInstanceName="testnotebook")
#
# print(response)

# "collection": "true",
# "annotation": "false",
# "zipCollection": "false"

# import requests
# import json
#
data = {"collections":[{
	"collectionId": "3cf81dfe-1d27-4c7f-9cbb-c7554decb821",
    "collection": "true",
    "collectionName":"testname"
}]

}




# import requests,json
# data1 = {
# 	"collectionIds": [
# 		"6379e9f7-f0ce-4a6e-9425-0b08a083f11c"
# 		],
# 		"orgId": "82709dd1-8924-481c-9d93-14a9e2e0c524"
# }
#
#
# headers = {"Content-Type":"application/json",
# "Authorization":"Bearer eyJraWQiOiJ1cy13ZXN0LTIxIiwidHlwIjoiSldTIiwiYWxnIjoiUlM1MTIifQ.eyJzdWIiOiJ1cy13ZXN0LTI6NGNjYjMyNWYtNDlhYi00YmQ1LWFmY2QtYWE4ODhkZDY3OWYxIiwiYXVkIjoidXMtd2VzdC0yOjJlNzdjM2JkLTYyMDQtNDEwMi1hNTI0LTRmYmJjYTRkZmY4NiIsImFtciI6WyJhdXRoZW50aWNhdGVkIiwiY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20vdXMtd2VzdC0yX3F2bXVQYzR2WSIsImNvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tL3VzLXdlc3QtMl9xdm11UGM0dlk6Q29nbml0b1NpZ25JbjpjY2FjZDM0Ny0yZjA3LTRiNzYtOGIwOC03NmIwYWY5MDhkYjQiXSwiaXNzIjoiaHR0cHM6Ly9jb2duaXRvLWlkZW50aXR5LmFtYXpvbmF3cy5jb20iLCJleHAiOjE1NzQ5NDM2NTcsImlhdCI6MTU3NDk0MzA1N30.YgoeA-IzdILKZM-azIqUukfxQbK_bxg76mD8lpVwr2K4LRDm4uSTEgrRP4fVg-RAxly0xVKPE71eSJ38SmSEjUlKDCzoAn43JMJcjk7gft0NFtyGWv6ICfwKfa0tYF3P3_VGmkKApegXh7GLu2unbL8CthwaFZykzaJMU28yd_b8Ty3fUFadx63OJVj_lAdYnmQbdgAKswhUuItmo6f8ytNa4Q-9eY5vdIdW2H9ziyWhJx1Yvg2NcGQWR_8u6nyJfZmawqrBRBdbAosTmuXiWElLtkR3W3hVFeiTwc9DHVIK_easFIyqRUgTRqSqQU7DPJHSLDgstV-0xF5v0x1QbQ"}
# r = requests.post(url='https://htnqwf8003.execute-api.us-west-2.amazonaws.com/dev_eai_tsdcsapi1/v1/collection-export?orgId=82709dd1-8924-481c-9d93-14a9e2e0c524',
#                   headers=headers,
#                   data=json.dumps(data))
#
# print(r.json())
# print(r.status_code)
#
# if r.status_code != 200:
#     print("Failed")
# else:
#     print("Success")


# import logging
#
# LOG = logging.getLogger("NotebookManager")
# # LOG.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG)
#
# LOG.setLevel(level=logging.DEBUG)
# LOG.info(" This is an info ")
# LOG.debug(" This is debug ")
# LOG.error(" This is an error ")


import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization' : 'Bearer eyJraWQiOiJ1cy13ZXN0LTIxIiwidHlwIjoiSldTIiwiYWxnIjoiUlM1MTIifQ.eyJzdWIiOiJ1cy13ZXN0LTI6NGNjYjMyNWYtNDlhYi00YmQ1LWFmY2QtYWE4ODhkZDY3OWYxIiwiYXVkIjoidXMtd2VzdC0yOjJlNzdjM2JkLTYyMDQtNDEwMi1hNTI0LTRmYmJjYTRkZmY4NiIsImFtciI6WyJhdXRoZW50aWNhdGVkIiwiY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20vdXMtd2VzdC0yX3F2bXVQYzR2WSIsImNvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tL3VzLXdlc3QtMl9xdm11UGM0dlk6Q29nbml0b1NpZ25JbjpjY2FjZDM0Ny0yZjA3LTRiNzYtOGIwOC03NmIwYWY5MDhkYjQiXSwiaXNzIjoiaHR0cHM6Ly9jb2duaXRvLWlkZW50aXR5LmFtYXpvbmF3cy5jb20iLCJleHAiOjE1NzYxNTUxNDAsImlhdCI6MTU3NjE1NDU0MH0.FlfACea7yjjNoOTeiSqlGGj_13ul3QGnaGvM0g0S7MtzVuEB823FKIuwtGOt1iKE4vm-4FVD-jz_rpYycO2M2QCPfvtd29keViUGaPrUY8RO5gMK1dI8wJ-RR3Km4tZY_LHWvZyoq1onOt7g3aYTbjq_P8602mJSG-8AT5IVFEEUri4ONKQxz0mtHg_xE08HpFurajYh-FmMprvNiSh8oiw-78JbExFewD8VxXvURc3yjApSQkk3XzoqAIoFAar8VbnIj88PKaHJyLbdmwUBvPt41oL_TCN8f6Gn623iw_9jb2L2VQvYeY4QzJaXRJeBo2cmtFQDmLi7uf10Mstz5g'
}

json_response = requests.get("https://core.prdge.us-west-2.eng.gehealthcloud.io/idam_uomapi/v2/user/me?detailed=true&orgrole=false",
                             headers=headers).json()


#print(json_response['userEntityAppRoles'])

my_roles_list = ['abc']

# for records in json_response['userEntityAppRoles']:
#     if records['entityName'] == 'Edison AI':
#         roles = records['roles']
#         final_org = records['parentOrganization']['id']
#         print(" The role is ", roles)
#         print(" The orgid is ", final_org)
#         for role in roles:
#             # if role['code'] in my_roles_list:
#             #     print(" Permission granted {} ".format(role['code']))
#             # else:
#             #     print(" Permission denied {} ".format(role['code']))
#
#             if not any(myrole in role['code'] for myrole in my_roles_list):
#                 print(" Permission denied for {} ".format(role['code']))
#             else:
#                 print(" Permission granted for {} ".format(role['code']))

roles_list = []
for entity in json_response['userEntityAppRoles']:
    if entity['entityName'] == 'Edison AI1':
        roles = entity['roles']
        user_org = entity['parentOrganization']['id']
        for role in roles:
            roles_list.append(role['code'])
if user_org and roles_list:
    resp = {'roles': roles_list,
        'user_org': user_org}
    resp['user_id'] = '{0} {1}'.format(json_response['givenName'], json_response['familyName'])

print(resp)

if not any(role in resp['roles'] for role in my_roles_list):
    print(" Access Denied ")




