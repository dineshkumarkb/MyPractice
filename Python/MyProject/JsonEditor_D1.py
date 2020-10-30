#Author : Dinesh
import Tkinter
import tkMessageBox
from Tkinter import *
import shutil,os,subprocess
from subprocess import PIPE,Popen


class MyProject:

    # Specify the URL of the path where JSON file is located. This is required only once
    myurl = "C:\Users\indkumar05\Desktop\orange_configs_sdk.json"

    def myjsonchange(self):
        """ This script is to change the contents of the json file with ease """
          
        json_open = open(MyProject.myurl,"r+")
        json_read = json_open.read()
        #json_open.truncate()
		
        # check for the preroll and enable if disabled and vice-versa
        if json_read.find("noroll") > 0:
           json_read = json_read.replace("noroll","preroll")
           tkMessageBox.showinfo("Success","Preroll is enabled")
        elif json_read.find("preroll") > 0:
           json_read = json_read.replace("preroll","noroll")
           tkMessageBox.showinfo("Success","Noroll is enabled")
        else:
      	   json_read = json_read.replace("midroll","preroll")		
           tkMessageBox.showinfo("Success","Preroll is enabled")
                
		# Write the changes to the json file
        json_open = open(MyProject.myurl,"r+")
        json_open.truncate()        
        json_open.write(json_read)
        json_open.close()
		
    def midrollchange(self):
        """ This script is to change the contents of the json file with ease """
		
        # Open the json file and read it
        json_open = open(MyProject.myurl,"r+")
        json_read = json_open.read()
        #json_open.truncate()    
   
       # Read the adtype in the json file and enabled/disable midroll
        if json_read.find("noroll") > 0:
           json_read = json_read.replace("noroll","midroll")
           tkMessageBox.showinfo("Success","Midroll is enabled")
        elif json_read.find("preroll") > 0:
           json_read = json_read.replace("preroll","midroll")
           tkMessageBox.showinfo("Success","Midroll is enabled")
        else:
           json_read = json_read.replace("midroll","noroll")
           tkMessageBox.showinfo("Success","Noroll is enabled")
		   
        # Write the changes to the json file
        json_open = open(MyProject.myurl,"r+")
        json_open.truncate()
        json_open.write(json_read)
        json_open.close()
	    
    def gatewaychange(self):
        """ Toggle the gateway url to wrong gateway and vice-versa for testing purpose """
		
        # Open the json file and read it
        json_open = open(MyProject.myurl,"r+")
        json_read = json_open.read()
        #json_open.truncate()
        
		# Read for the URL in the json file.Ex if touchstone URL is found, replace with badgateway URL
        if json_read.find("http://touchstone.conviva.com") > 0:
           json_read = json_read.replace("http://touchstone.conviva.com","https://cws.badcert.staging.conviva.com")
           tkMessageBox.showinfo("Gateway Change","Gateway https://cws.badcert.staging.conviva.com has been set")
        else:
           json_read = json_read.replace("https://cws.badcert.staging.conviva.com","http://touchstone.conviva.com")
           tkMessageBox.showinfo("Gateway Change","Gateway : http://touchstone.conviva.com has been set")
        
		# Write the changes to the json file
        json_open = open(MyProject.myurl,"r+")	
        json_open.truncate()        
        json_open.write(json_read)
        json_open.close()
        
    def copytodevice(self):
        """Copy the json file into the android device"""
        
        #shutil.copy(s,d)
        #subprocess.Popen([adb, 'push', s, d], stdout=subprocess.PIPE).communicate()
        cmd = "adb push C:\Users\indkumar05\Desktop\orange_configs_sdk.json /mnt/sdcard/"
        p = Popen(cmd,stderr = PIPE)
        subprocess.Popen(cmd)
        a = p.communicate()
        print a
        if "error" in a:
            tkMessageBox.showinfo("Error!","Error copying the files. Please check if your device is connected")
        else:
            tkMessageBox.showinfo("Success","Error copying the files. Please check if your device is connected")     
        
        
		
# Create objects for GUI and MyProject    
prerollchange = MyProject()
t = Tkinter.Tk()

# Create Preroll button and call the corresponding function
preroll_en = Tkinter.Button(t, text = "Toggle Preroll On/Off",command = prerollchange.myjsonchange)
preroll_en.grid(row = 0)

# Create Gateway Change button and call the corresponding function
gateway_en = Tkinter.Button(t, text = "Toggle Wrong Gateway",command = prerollchange.gatewaychange)
gateway_en.grid(row = 1)

# Create Midroll button and call the corresponding function
midroll_en = Tkinter.Button(t, text = "Toggle Midroll On/Off",command = prerollchange.midrollchange)
midroll_en.grid(row = 3)

copy_device = Tkinter.Button(t, text = "Copy to Device",command = prerollchange.copytodevice)
copy_device.grid(row = 4)

t.mainloop()
