#Author : Dinesh
#Last Modified:25-08-2015
import Tkinter
import tkMessageBox
from Tkinter import *
import subprocess
from subprocess import PIPE,Popen
from tkFileDialog import askopenfilename


class MyProject:

    # Specify the URL of the path where JSON file is located. This is required only once
    myurl = "C:\JsonEditor\orange_configs_sdk.json"
    #myurl = "C:\JsonEditor\orange_static.json"
    #print myurl_test
    
    def setfilepath(self,path):
        self.myurl = path 
        print self.myurl
               
    def prerollchange(self):
        """ This script is to change the contents of the json file with ease """
        # Open the json file and read it  
        json_open = open(MyProject.myurl,"r+")
        json_read = json_open.read()
        
        # Read the adtype in the json file and toggle preroll/noroll
        if "preroll" in json_read:
            json_read = json_read.replace("preroll","noroll")            
            tkMessageBox.showinfo("Success","Noroll is enabled")        
        elif "postroll" in json_read:
            json_read = json_read.replace("postroll","preroll")
            tkMessageBox.showinfo("Success","Preroll is enabled")
        elif "midroll" in json_read:
            json_read = json_read.replace("midroll","preroll")
            tkMessageBox.showinfo("Success","Preroll is enabled")
        elif "noroll" in json_read:
            json_read = json_read.replace("noroll","preroll")
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
        if "preroll" in json_read:
            json_read = json_read.replace("preroll","midroll")            
            tkMessageBox.showinfo("Success","Midroll is enabled")        
        elif "postroll" in json_read:
            json_read = json_read.replace("postroll","midroll")
            tkMessageBox.showinfo("Success","Midroll is enabled")
        elif "midroll" in json_read:
            json_read = json_read.replace("midroll","noroll")
            tkMessageBox.showinfo("Success","Noroll is enabled")
        elif "noroll" in json_read:
            json_read = json_read.replace("noroll","midroll")
            tkMessageBox.showinfo("Success","Midroll is enabled")
		   
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
        if "http://touchstone.conviva.com" in json_read:
           json_read = json_read.replace("http://touchstone.conviva.com","https://cws.badcert.staging.conviva.com")
           tkMessageBox.showinfo("Gateway Change","Gateway https://cws.badcert.staging.conviva.com has been set")
        elif "https://touchstone.conviva.com" in json_read:
           json_read = json_read.replace("https://touchstone.conviva.com","https://cws.badcert.staging.conviva.com")
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
        
        
        # Store the adb command
        cmd = "adb push C:\JsonEditor\orange_configs_sdk.json /mnt/sdcard/"
        p = Popen(cmd,stderr = PIPE)
        
        # Pass the adb command to the system through subprocess
        subprocess.Popen(cmd)
        a = p.communicate()
        
        # Check for the errors if any else copy the json file to the device
        if "error: device not found" in str(a):
            tkMessageBox.showinfo("Error","Error copying the files" " "  +a[1])
        else:
            tkMessageBox.showinfo("Success","Your files have been copied to the device successfully")       
        
# Create objects for GUI and MyProject    
jsonchange = MyProject()
t = Tkinter.Tk()
t.wm_title("JSON_EDITOR")

# Create Preroll button and call the corresponding function
preroll_en = Tkinter.Button(t, text = "TOGGLE PREROLL/NOROLL",height = 2,justify = CENTER,width = 30,command = jsonchange.prerollchange)
preroll_en.grid(row = 0)

# Create Gateway Change button and call the corresponding function
gateway_en = Tkinter.Button(t, text = "TOGGLE GATEWAY",height = 2,justify = CENTER,width = 30,command = jsonchange.gatewaychange)
gateway_en.grid(row = 1)

# Create Midroll button and call the corresponding function
midroll_en = Tkinter.Button(t, text = "TOGGLE MIDROLL/NOROLL",height = 2,justify = CENTER,width = 30,command = jsonchange.midrollchange)
midroll_en.grid(row = 3)

# Create copy to device button and call corresponding function
copy_device = Tkinter.Button(t, text = "COPY TO DEVICE",height = 2,justify = CENTER,width = 30,command = jsonchange.copytodevice)
copy_device.grid(row = 4)

# Create copy to device button and call corresponding function
postroll_en = Tkinter.Button(t, text = "TOGGLE POSTROLL/NOROLL",height = 2,justify = CENTER,width = 30,state = DISABLED)
postroll_en.grid(row = 5)

myurl = askopenfilename()
b = Button(t,text = "Browse",command = myurl)
b.grid(row = 6)

jsonchange.setfilepath(myurl)

t.mainloop()

"""
jsonchange = MyProject()
t = Tkinter.Tk()
t.wm_title("JSON_EDITOR")

tv = StringVar()
label_path = Label(t,text = "JSON_PATH",width = 8)
label_path.grid()

path_en = Entry(t,textvariable = tv,justify = RIGHT,width = 30)
path_en.grid()

myurl_test = path_en.get()
print dir(MyProject)


#getpath()


"""