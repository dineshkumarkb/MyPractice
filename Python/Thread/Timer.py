"""
This is to illustrate a timer in python.
Uses : Call a method every second/every minute to update something.
Example : Like a progress bar
"""

from threading import Timer
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

class MyTimer:

    def __init__(self,timegap = 1):

        self.timegap = timegap

    def callme(self):
        print " This is callme " ,datetime.datetime.now().time()


t = MyTimer()

s =  BackgroundScheduler()
s.add_job(t.callme)
s.start()