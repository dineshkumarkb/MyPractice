#Application Name : JSONEDITOR
#Author : DineshKumar K B
#Date : 22-01-2016
#Modified : 22-01-2016
#Version : 2.0


import re,os
import wx
import subprocess
from subprocess import Popen,PIPE
from my_ui import *


class TestReplace:


    def __init__(self,json_path = None,apk_path = None):
        """
        :param json_path:
        :param apk_path:
        :return: None
        json_path and apk_path should be passed while creating the contructor for TestReplace Class
        It is passed from my_ui.py file
        """

        # Assign the parameters to the current instance
        self.json_path = json_path
        self.apk_path = apk_path


    @staticmethod
    def readfromfile(json_path):
        """
        :param json_path:
        :return: myjsonread
        This method will be called each time the json file has to be read. It will return the read string
        """

        # This check is to ensure that the user has selected the json file path
        if json_path is not None:
           myjsonopen = open(json_path,"r+")
           myjsonopen.seek(0,0)
           myjsonread = myjsonopen.read()
           myjsonopen.close()
           return myjsonread


    @staticmethod
    def writetofile(preplace,json_path):
        """
        :param preplace:
        :param json_path:
        :return: True
        This method will be called each time contents has to be written to the file. It will
        return true after writing to the file
        """
        myjsonopen = open(json_path,"r+")

        # This is necessary to ensure the file contents are cleared before writing to avoid overlap
        myjsonopen.truncate()
        myjsonopen.seek(0,0)

        # preplace param will be passed from the method that is calling writetofile.
        # That will contain the modified string
        myjsonopen.write(preplace)
        myjsonopen.close()

        # Returns true after writing to the file
        return True

    @staticmethod
    def adbdevicescheck():
        """
        This method is to validate if an adb device is connected to the PC.
        Returns a boolean value based on the availability of the device
        """

        # Create a Popen instance and pass the commands
        p = subprocess.Popen("adb devices",stdout=PIPE,stderr=PIPE,shell= True)
        a = p.communicate()

        # Convert the tuple output to a string anf check if the device is
        # online.
        a = str(a).split()
        if ("device" or "unuthorized" or "offline") in a[4]:
            return True
        else:
            return False

    @staticmethod
    def jsoncontentscheck(json_path):
        """
        :param json_path:
        :return: Boolean
        This method is to check if the json path is available and then returns True is available
        """
        if json_path is None:
           wx.MessageBox("Please choose a JSON File","Error")
           return False
        else:
            return True

    def myprerollreplace(self,event):
        """
        :param event:
        This method is to replace the preroll in the adType
        """

        # Read the json contents
        self.myjsonread = TestReplace.readfromfile(self.json_path)

        # If the jsonpath is available, proceed. Else throw an error message
        # Though this is not required as the buttons will not be enabled its a double check.
        if TestReplace.jsoncontentscheck(self.json_path) == True:
           prerollpattern = r'("adType")\s*:\s*(".+",)'
           if len(re.findall(prerollpattern,self.myjsonread)) > 0:
              prerollreplace = re.sub(prerollpattern,r'\1: "preroll",',self.myjsonread)
              self.status_check = TestReplace.writetofile(prerollreplace,self.json_path)
              if self.status_check == True:
                 wx.MessageBox("Preroll Has Been Enabled","Success")
           else:
              wx.MessageBox("Ad Type was not found","Error")

    def mymidrollreplace(self,event):
        """
        :param event:
        This method is to replace the midroll in the adType
        """

        # Read the json contents
        self.myjsonread = TestReplace.readfromfile(self.json_path)

        if TestReplace.jsoncontentscheck(self.json_path) == True:
           midrollpattern = r'("adType")\s*:\s*(".+",)'
           if len(re.findall(midrollpattern,self.myjsonread)) > 0:
              midrollreplace = re.sub(midrollpattern,r'\1: "midroll",',self.myjsonread)
              self.status_check = TestReplace.writetofile(midrollreplace,self.json_path)
              if self.status_check == True:
                 wx.MessageBox("Midroll Has Been Enabled","Success")
           else:
              wx.MessageBox("Ad Type Not Found","Error")

    def mypostrollreplace(self,event):
        """
        :param event:
        This method is to replace the postroll in the adType
        """

        # Read the json contents
        self.myjsonread = TestReplace.readfromfile(self.json_path)

        if TestReplace.jsoncontentscheck(self.json_path) == True:
           postrollpattern = r'("adType")\s*:\s*(".+",)'
           if len(re.findall(postrollpattern,self.myjsonread)) > 0:
              postrollreplace = re.sub(postrollpattern,r'\1: "postroll",',self.myjsonread)
              self.status_check = TestReplace.writetofile(postrollreplace,self.json_path)
              if self.status_check == True:
                  wx.MessageBox("Postroll Has Been Enabled","Success")
           else:
              wx.MessageBox("Ad Type Not Found","Error")

    def mynorollreplace(self,event):
        """
        :param event:
        This method is to replace noroll in the adType
        """

        # Read the json contents
        self.myjsonread = TestReplace.readfromfile(self.json_path)

        if TestReplace.jsoncontentscheck(self.json_path) == True:
           norollpattern = r'("adType")\s*:\s*(".+",)'
           if len(re.findall(norollpattern,self.myjsonread)) > 0:
              norollreplace = re.sub(norollpattern,r'\1: "noroll",',self.myjsonread)
              self.status_check = TestReplace.writetofile(norollreplace,self.json_path)
              if self.status_check == True:
                 wx.MessageBox("Noroll Has Been Enabled","Success")
           else:
              wx.MessageBox("Ad Type not Found","Error")


    def myadbinstall(self,event):
        """
        :param event:
        This method is to will perform adb install through subprocess.Popen method
        """

        # This check is required because adb install keeps waiting until a device is connected
        # This will make the application crash
        if TestReplace.adbdevicescheck()== True:

            # store the adb install command in a variable
            adbcmd = r'adb install -r {}'.format(self.apk_path)
            p = subprocess.Popen(adbcmd, shell=True, stdout= PIPE, stderr= PIPE)
            a = p.communicate()
            # Check for the returncode of the Popen Object to check if the call was successful
            if p.returncode == 0:
               wx.MessageBox("Adb install success","Success")
            else:
               wx.MessageBox(a[1],"Error")
        else:
            wx.MessageBox("Please check if your device is connected","Error")


    def myadbreboot(self,event):
        """
        :param event:
        This method is called to reboot the adb device
        """
        adbcmd = r'adb reboot'
        p = subprocess.Popen(adbcmd,shell=True,stderr= PIPE,stdout=PIPE)
        a = p.communicate()
        if p.returncode == 0:
           wx.MessageBox("Adb Reboot success","Device Rebooted")
        else:
            wx.MessageBox(a[1],"Error")



    def myadbpush(self,event):
        """
        :param event:
        This method will be called when adbpush button is clicked
        """
        adbcmd = r'adb push {} /mnt/sdcard/'.format(self.json_path)
        p = subprocess.Popen(adbcmd,shell = True,stderr=PIPE,stdout=PIPE)
        a = p.communicate()
        if p.returncode == 0:
            wx.MessageBox("The files have been pushed to the devices","Success")
        else:
            wx.MessageBox(a[1],"Error")


    def myHLSVODbipbop(self,event):
        """
        :param event:
        This method will be called when HLS VOD has to be replaced. This will check for the content source and
        replace with the bipbop URL
        """

        self.myjsonread = TestReplace.readfromfile(self.json_path)
        hlsvodpat = r'("contentSrc")\s*:\s*("http://.+"),'
        if len(re.findall(hlsvodpat,self.myjsonread)) > 0:
           hlsvodcopy = re.sub(hlsvodpat,
                            r'\1: "http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",',
                            self.myjsonread,1)
           self.status_check = TestReplace.writetofile(hlsvodcopy,self.json_path)
           if self.status_check == True:
              wx.MessageBox("URL http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8 has been set",
                            "URL CHANGE")
        else:
            wx.MessageBox("ContentSource Field was not found in your JSON File","Error")


    def myHLSVODipadakamai(self,event):
        """
        :param event:
        This method will be called when HLS VOD has to be replaced. This will check for the content source and
        replace with the ipad akamai URL
        """

        self.myjsonread = TestReplace.readfromfile(self.json_path)
        hlsvodpat = r'("contentSrc")\s*:\s*("http://.+"),'
        if len(re.findall(hlsvodpat,self.myjsonread)) > 0:
           hlsvodcopy = re.sub(hlsvodpat,
                            r'\1: "http://ipad.akamai.com/Video_Content/npr/cherryblossoms_hdv_bug/all.m3u8",',
                            self.myjsonread,1)
           self.status_check = TestReplace.writetofile(hlsvodcopy,self.json_path)
           if self.status_check == True:
              wx.MessageBox("URL http://ipad.akamai.com/Video_Content/npr/cherryblossoms_hdv_bug/all.m3u8 has been set",
                            "URL CHANGE")
        else:
            wx.MessageBox("ContentSource Field was not found in your JSON File","Error")

    def myHLSVODqhttp(self,event):
        """
        :param event:
        This method will be called when HLS VOD has to be replaced. This will check for the content source and
        replace with the QHTTP URL
        """

        self.myjsonread = TestReplace.readfromfile(self.json_path)
        hlsvodpat = r'("contentSrc")\s*:\s*("http://.+"),'
        if len(re.findall(hlsvodpat,self.myjsonread)) > 0:
           hlsvodcopy = re.sub(hlsvodpat,
                               r'\1: "http://qthttp.apple.com.edgesuite.net/1010qwoeiuryfg/sl.m3u8",',
                               self.myjsonread,1)
           self.status_check = TestReplace.writetofile(hlsvodcopy,self.json_path)
           if self.status_check == True:
               wx.MessageBox("URL http://qthttp.apple.com.edgesuite.net/1010qwoeiuryfg/sl.m3u8","URL CHANGE")
        else:
            wx.MessageBox("ContentSource Field was not found in your JSON File","Error")


    def myHLSLIVEbipbop(self,event):
        """
        :param event:
        This method will be called when HLS LIVE has to be replaced. This will check for the content source and
        replace with the BIPBOP LIVE URL
        """

        self.myjsonread = TestReplace.readfromfile(self.json_path)
        hlslivepat = r'("contentSrc")\s*:\s*("http://.+"),'
        if len(re.findall(hlslivepat,self.myjsonread)) > 0:
           hlslivecopy = re.sub(hlslivepat,
                                r'\1: "http://demo.irdetodemos.com/LiveBipBopAll/bipbopall.m3u8",',
                                self.myjsonread,1)
           if TestReplace.writetofile(hlslivecopy,self.json_path) == True:
              wx.MessageBox("URL http://demo.irdetodemos.com/LiveBipBopAll/bipbopall.m3u8","URL CHANGE")
        else:
            wx.MessageBox("ContentSource Field was not found in your JSON File","Error")

    def myHLSLIVEvevo(self,event):
        """
        :param event:
        This method will be called when HLS LIVE has to be replaced. This will check for the content source and
        replace with the VEVO LIVE URL
        """

        self.myjsonread = TestReplace.readfromfile(self.json_path)
        hlslivepat = r'("contentSrc")\s*:\s*("http://.+"),'
        if len(re.findall(hlslivepat,self.myjsonread)) > 0:
           hlslivecopy = re.sub(hlslivepat,
                             r'\1: "http://vevoplaylist-live.hls.adaptive.level3.net/vevo/ch1/appleman.m3u8",',
                             self.myjsonread,1)
           if TestReplace.writetofile(hlslivecopy,self.json_path) == True:
              wx.MessageBox("URL http://vevoplaylist-live.hls.adaptive.level3.net/vevo/ch1/appleman.m3u8 has been set",
                            "URL CHANGE")
        else:
            wx.MessageBox("ContentSource Field was not found in your JSON File","Error")



    def mySSbigbunny(self,event):
        """
        :param event:
        This method will be called when SS VOD has to be replaced. This will check for the content source and
        replace with the BB URL
        """
        self.myjsonread = TestReplace.readfromfile(self.json_path)
        ssvodpat = r'("contentSrc")\s*:\s*("http://.+"),'

        # If content src tag is not available in json file this will handle that
        if len(re.findall(ssvodpat,self.myjsonread)) == 0:
            wx.MessageBox("contentSrc Field was not found in your JSON File","Error")
            return

        elif len(re.findall(ssvodpat,self.myjsonread)) == 3:
           ssvodcopy = re.finditer(ssvodpat,self.myjsonread)
           count = 1
           for matchedstring in ssvodcopy:
               if count == 2:
                  #ssstring = matchedstring.group(0)
                  ssvodreplace = re.sub(matchedstring.group(0),
                                    r'"contentSrc": "http://iis7test.entriq.net/Clr/Big_Buck_Bunny.ism/Manifest",'
                                    ,self.myjsonread,1)
               # This count should not be given in else part because after count == 2 it will not increment and
               # again it will replace the third URL
               count+=1

        else:
            ssvodreplace = re.sub(ssvodpat,r'"contentSrc": "http://iis7test.entriq.net/Clr/Big_Buck_Bunny.ism/Manifest",'
                               ,self.myjsonread)

        if TestReplace.writetofile(ssvodreplace,self.json_path):
           wx.MessageBox("http://iis7test.entriq.net/Clr/Big_Buck_Bunny.ism/Manifest URL Set","SS URL SET")



    def mySSLIVE(self,event):
        """
        :param event:
        This method will be called when SS LIVE has to be replaced. This will check for the content source and
        replace with the BB URL
        """
        self.myjsonread = TestReplace.readfromfile(self.json_path)
        sslivepat = r'("contentSrc")\s*:\s*("http://.+"),'

        if len(re.findall(sslivepat,self.myjsonread)) == 0:
            wx.MessageBox("ContentSource Field was not found in your JSON File","Error")
            return
        if len(re.findall(sslivepat,self.myjsonread)) == 3:
           sslivecopy = re.finditer(sslivepat,self.myjsonread)
           count = 1
           for matchedstring in sslivecopy:
               if count == 2:
                  ssstring = matchedstring.group(0)
                  sslivereplace = re.sub(ssstring,
                                         r'"contentSrc": "http://vevoplaylist-live.hss.adaptive.level3.net:80/livefeed/vevo/ch1.isml/Manifest",'
                                         ,self.myjsonread,1)
                  if TestReplace.writetofile(sslivereplace,self.json_path):
                      wx.MessageBox("http://vevoplaylist-live.hss.adaptive.level3.net:80/livefeed/vevo/ch1.isml/Manifest",
                                    "SS LIVE URL SET")
               count+=1

        else:
            sslivereplace = re.sub(sslivepat,
                                   r'"contentSrc": "http://vevoplaylist-live.hss.adaptive.level3.net:80/livefeed/vevo/ch1.isml/Manifest",',
                                   self.myjsonread)
            if TestReplace.writetofile(sslivereplace,self.json_path):
               wx.MessageBox("http://vevoplaylist-live.hss.adaptive.level3.net:80/livefeed/vevo/ch1.isml/Manifest",
                             "SS LIVE URL SET")



    def mySSLIVESlight(self,event):
        """
        :param event:
        This method will be called when SS LIVE has to be replaced. This will check for the content source and
        replace with the BB URL
        """

        self.myjsonread = TestReplace.readfromfile(self.json_path)
        sslivepat = r'("contentSrc")\s*:\s*("http://.+"),'
        if len(re.findall(sslivepat,self.myjsonread)) == 0:
            wx.MessageBox("ContentSource Field was not found in your JSON File","Error")
            return
        if len(re.findall(sslivepat,self.myjsonread)) == 3:
           sslivecopy1 = re.finditer(sslivepat,self.myjsonread)
           count = 1
           for matchedstring in sslivecopy1:
               if count == 2:
                  ssstring = matchedstring.group(0)
                  sslivereplace1 = re.sub(ssstring,
                                         r'"contentSrc": "http://silverlight.envivio.com/subtitles.isml/manifest",'
                                         ,self.myjsonread,1)
                  if TestReplace.writetofile(sslivereplace1,self.json_path):
                      wx.MessageBox("http://silverlight.envivio.com/subtitles.isml/manifest","SS LIVE URL SET")
               count+=1

        else:
            sslivereplace1 = re.sub(sslivepat,
                                   r'"contentSrc": "http://silverlight.envivio.com/subtitles.isml/manifest",',
                                   self.myjsonread)
            
            if TestReplace.writetofile(sslivereplace1,self.json_path):
                wx.MessageBox("http://silverlight.envivio.com/subtitles.isml/manifest","SS LIVE URL SET")



    def myMP4livepass(self,event):
        """
        :param event:
        This method is used to set the mp4 URL envato. All URLs will be set to livepass if the number of
         protocols in JSON file are any number other than 3. Else only the 3rd will be set.
        """

        self.myjsonread = TestReplace.readfromfile(self.json_path)
        mp4pat = r'("contentSrc")\s*:\s*("http://.+"),'
        if len(re.findall(mp4pat,self.myjsonread)) == 0:
            wx.MessageBox("ContentSource Field was not found in your JSON File","Error")
            return
        if len(re.findall(mp4pat,self.myjsonread)) == 3:
           mp4copy = re.finditer(mp4pat,self.myjsonread)
           count = 1
           for matchedstring in mp4copy:
               if count == 3:
                  mp4string = matchedstring.group(0)
                  mp4replace = re.sub(mp4string,
                                    r'"contentSrc":"http://livepassdl.staging.conviva.com/vod/sintel-long-900.mp4",'
                                    ,self.myjsonread,1)
                  if TestReplace.writetofile(mp4replace,self.json_path):
                      wx.MessageBox("Live Pass MP4 URL has been set","Success")
               count+=1

        else:
            mp4replace = re.sub(mp4pat,
                                r'"contentSrc":"http://livepassdl.staging.conviva.com/vod/sintel-long-900.mp4",',
                                self.myjsonread)
            if TestReplace.writetofile(mp4replace,self.json_path):
                wx.MessageBox("Live Pass MP4 URL has been set","Success")

    def myMP4envato(self,event):
        """
        :param event:
        This method is used to set the mp4 URL envato. All URLs will be set to envato if the number of
         protocols in JSON file are any number other than 3. Else only the 3rd will be set.
        """

        self.myjsonread = TestReplace.readfromfile(self.json_path)
        mp4pat = r'("contentSrc")\s*:\s*("http://.+"),'
        if len(re.findall(mp4pat,self.myjsonread)) == 0:
            wx.MessageBox("ContentSource Field was not found in your JSON File","Error")
            return
        if len(re.findall(mp4pat,self.myjsonread)) == 3:
           mp4copy1 = re.finditer(mp4pat,self.myjsonread)
           count = 1
           for matchedstring in mp4copy1:
               if count == 3:
                  mp4string = matchedstring.group(0)
                  mp4replace1 = re.sub(mp4string,
                                    r'"contentSrc":"http://0.s3.envato.com/h264-video-previews/80fad324-9db4-11e3-bf3d-0050569255a8/490527.mp4",'
                                    ,self.myjsonread,1)
                  if TestReplace.writetofile(mp4replace1,self.json_path):
                      wx.MessageBox("Envato URL has been set","Success")
               count+=1

        else:
            mp4replace1 = re.sub(mp4pat,
                                r'"contentSrc":"http://0.s3.envato.com/h264-video-previews/80fad324-9db4-11e3-bf3d-0050569255a8/490527.mp4",',
                                self.myjsonread)
            if TestReplace.writetofile(mp4replace1,self.json_path):
                wx.MessageBox("Envato URL has been set","Success")


    def myHLSad(self,event):
        """
        :param event:
        This method is used to set a HLS ad URL
        """

        self.myjsonread = TestReplace.readfromfile(self.json_path)
        hlsadpat = r'("adUrl")\s*:\s*("http://.+"),*'
        if len(re.findall(hlsadpat,self.myjsonread)) > 0:
           hlsadcopy = re.sub(hlsadpat,
                            r'\1: "http://ipad.akamai.com/Video_Content/npr/cherryblossoms_hdv_bug/all.m3u8"',
                            self.myjsonread)
           if TestReplace.writetofile(hlsadcopy,self.json_path):
              wx.MessageBox("URL http://ipad.akamai.com/Video_Content/npr/cherryblossoms_hdv_bug/all.m3u8 has been set",
                            "URL CHANGE")
        else:
            wx.MessageBox("AD URL Field was not found in your JSON File","Error")


    def mySSad(self,event):
        """
        :param event:
        This method is used to set a SS ad URL
        """

        self.myjsonread = TestReplace.readfromfile(self.json_path)
        ssadpat = r'("adUrl")\s*:\s*("http://.+"),*'
        if len(re.findall(ssadpat,self.myjsonread)) > 0:
           ssadcopy = re.sub(ssadpat,
                            r'\1: "http://iis7test.entriq.net/Clr/Big_Buck_Bunny.ism/Manifest"',
                            self.myjsonread)
           if TestReplace.writetofile(ssadcopy,self.json_path):
              wx.MessageBox("URL http://iis7test.entriq.net/Clr/Big_Buck_Bunny.ism/Manifest",
                            "URL CHANGE")
        else:
            wx.MessageBox("AD URL Field was not found in your JSON File","Error")


    def mymp4ad(self,event):
        """
        :param event:
        This method is used to set an mp4 ad URL
        """

        self.myjsonread = TestReplace.readfromfile(self.json_path)
        mp4adpat = r'("adUrl")\s*:\s*("http://.+"),*'
        if len(re.findall(mp4adpat,self.myjsonread)) > 0:
           mp4adcopy = re.sub(mp4adpat,
                            r'\1: "http://0.s3.envato.com/h264-video-previews/80fad324-9db4-11e3-bf3d-0050569255a8/490527.mp4"',
                            self.myjsonread)
           if TestReplace.writetofile(mp4adcopy,self.json_path):
              wx.MessageBox("URL http://0.s3.envato.com/h264-video-previews.mp4 has been set",
                      "URL CHANGE")
        else:
            wx.MessageBox("AD URL Field was not found in your JSON File","Error")

    def setbadgateway(self,event):
        """
        :param event:
        This method is used to set the bad gateway for bugzilla ID 4237
        """
        self.myjsonread = TestReplace.readfromfile(self.json_path)
        badgateway_patt = r'("cwsGateway"):\s*.+,'
        if (len(re.findall(badgateway_patt,self.myjsonread))) > 0:
           badgateway_copy = re.sub(badgateway_patt,r'\1: "https://cws.badcert.staging.conviva.com",',self.myjsonread)
           TestReplace.writetofile(badgateway_copy,self.json_path)
           wx.MessageBox("Bad Gateway Set","Gateway Change")
        else:
            wx.MessageBox("Cws Gateway not found","Error")


    def touchstonegateway(self,event):
        """
        :param event:
        This method is used to set the touchstone gateway for bugzilla ID 4237
        """

        self.myjsonread = TestReplace.readfromfile(self.json_path)
        badgateway_patt = r'("cwsGateway"):\s*.+,'
        if (len(re.findall(badgateway_patt,self.myjsonread))) > 0:
           badgateway_copy = re.sub(badgateway_patt,r'\1: "https://touchstone.conviva.com",',self.myjsonread)
           TestReplace.writetofile(badgateway_copy,self.json_path)
           wx.MessageBox("Touchstone gateway Set","Gateway Change")
        else:
            wx.MessageBox("Cws Gateway not found","Error")


    def setislivetrue(self,event):
        """
        :param event:
        This method is used to set the is live parameter in the JSON file to True
        irrespective of the current value
        """
        # Read from the json file and store the string in the variable
        self.myjsonread = TestReplace.readfromfile(self.json_path)
        islivepatt = r'("isLive")\s*:\s*(.+),'

        # Validate if the islive parameter is really available
        if len(re.findall(islivepatt,self.myjsonread)) > 0:
           islivereplace = re.sub(islivepatt,r'\1:true,',self.myjsonread)
           if TestReplace.writetofile(islivereplace,self.json_path):
               wx.MessageBox("Is Live Value Set to True","Success")
        else:
            wx.MessageBox("Is Live parameter not found","Error")

    def setislivefalse(self,event):
        """
        :param event:
        This method is used to set the is live parameter in the JSON file to false
        irrespective of the current value
        """

        # Read from the json file and store the string in the variable
        self.myjsonread = TestReplace.readfromfile(self.json_path)
        islivepatt = r'("isLive")\s*:\s*(.+),'

        # Validate if the islive parameter is really available
        if len(re.findall(islivepatt,self.myjsonread)) > 0:
           islivereplace = re.sub(islivepatt,r'\1:false,',self.myjsonread)
           if TestReplace.writetofile(islivereplace,self.json_path):
               wx.MessageBox("Is Live Value Set to False","Success")
        else:
            wx.MessageBox("Is Live parameter not found","Error")



