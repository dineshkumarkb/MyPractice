from subprocess import PIPE,Popen
import time,sys
from os import getcwd
import logging
import Tkinter as tk
import threading
import tkMessageBox

class MyUI(tk.Tk):

    """
    This class inherits the Tkinter module and implements the UI components
    All the UI components have been taken care in the constructor.
    This runs as a main thread. In this we create a secondary thread
    """

    def __init__(self,* args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title("Bandwith Test")
        self.geometry('250x75')
        self.resizable(width = False, height = False)

        self.label = tk.Label(text = "Frequency(seconds)")
        self.label.grid(row = 0, column = 0)

        self.entry = tk.Entry(bd = 5)
        self.entry.grid(row = 0, column = 1)

        self.button = tk.Button(text = "Start Test", command = self.callchildthread)
        self.button.grid(row = 1, column = 0)

        self.button = tk.Button(text = "Close App", command = lambda : sys.exit(0))
        self.button.grid(row = 1, column = 1)

        self.mainloop()


        print "Test End"

    def callchildthread(self):

        a = int(self.entry.get())
        thread1 = NetTest(a)
        thread1.start()
        tkMessageBox.showinfo("Logs Capture Started","The logs will be captured at {} seconds interval and will be saved in "
                                                     "{}".format(a,NetTest.writetoname))



class NetTest(threading.Thread):

    speedtestcmd = r'speedtest-cli'
    writetoname = getcwd()+"\\netlogs.log"

    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.interval = interval

    def run(self):

        self.main()

    def main(self):
        """
        The main function infinitely loops and connects to speedtest, determines the results and
        log the same in the frequency provided by the user.
        """

        domain = None
        downloadspeed = None
        uploadspeed = None

        try:

            while thread1.is_alive():

                p = Popen(NetTest.speedtestcmd,stdout = PIPE, stderr = PIPE, shell = True)
                a = p.communicate()[0].split("\n")
                for items in a:
                    if "Download:" in items:
                        downloadspeed = items
                    elif "Upload:" in items:
                        uploadspeed = items
                    elif "Testing from" in items:
                        domain = items

                logging.basicConfig(filename = NetTest.writetoname, filemode = "a+", level = logging.DEBUG)
                logging.info("----------------------------------------------")
                logging.info("The logs are captured on {}".format(time.asctime()))
                logging.info(domain)
                logging.info("The download speed is {}".format(downloadspeed))
                logging.info("The upload speed is {}".format(uploadspeed))
                logging.info("----------------------------------------------")
                time.sleep(self.interval)

        except KeyboardInterrupt as e:
            print "Exiting", e


thread1 = threading.Thread(target = MyUI)
thread1.start()








