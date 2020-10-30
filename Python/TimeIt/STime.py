from time import time
from datetime import datetime

class STime(object):

    start_time = 0
    stop_time = 0

    @staticmethod
    def start():
        #STime.start_time = time()
        STime.start_time =  datetime.now()

    @staticmethod
    def stop():
        #STime.stop_time = time()
        STime.stop_time = datetime.now()


    @staticmethod
    def get_start_time():
        return STime.start_time

    @staticmethod
    def get_stop_time():
        return STime.stop_time

    @staticmethod
    def get_interval():
        return STime.stop_time-STime.start_time


if __name__ == "__main__":
    STime.start()
    print STime.get_start_time()
    STime.stop()
    print STime.get_stop_time()
    print STime.get_interval()
