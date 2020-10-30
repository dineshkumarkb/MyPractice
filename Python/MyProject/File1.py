"""
#from File2 import *


class MyTest1:


    def add(self,a,b):

        return a + b

    def sub(self,a,b):

        return a - b



if __name__ == "__main__":

    m = MyTest1()
    print m.add(2,1)
    print m.sub(2,1)
   # print m.mul(2,1)
    print m.name

import os,re

class MyFileRead:

    def __init__(self):

        self.myfilepath = open("D:\orange_configs_sdk.json","r+")
        self.filecontents = self.myfilepath.read()

    def mychange(self):

        mypattern = r'"(adType)": "(.+)"'
        mymatch = re.sub(r'"(adType)": "(.+)"', r'"\1": "preroll"',self.filecontents)
        print mymatch

    def myurlchange(self):

        mypattern = r'"content.+": "http://.+",{1}'
        mymatch = re.sub(mypattern,r'"contentSrc": "http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",',self.filecontents)
        print mymatch




m = MyFileRead()
#m.mychange()
m.myurlchange()

"""

import xlsxwriter

xlsxwriter.Workbook.add_chart()