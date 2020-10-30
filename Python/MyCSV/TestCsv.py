import csv

class TestCsv:

    def __init__(self):
        self.file_path = r'C:\Users\indkumar05\Desktop\mycsv.csv'

    def readCSV(self):

        with open(self.file_path,'rb') as f:
            reader = csv.reader(f)
            data = list(reader)
        print data


t = TestCsv()
t.readCSV()

import requests, httplib, urllib2

class MyRequest: