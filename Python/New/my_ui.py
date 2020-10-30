#Application Name : JSONEDITOR
#Author : DineshKumar K B
#Date : 22-01-2016
#Modified : 22-01-2016
#Version : 2.0


import wx
import my_replace
from my_replace import *


# Store the jsonpath and apk path from the user into a dictionary.
# This will be used everywhere in the program. So this has to be available globally
mypaths = {"json_path" : None,"apk_path" : None}


# This method will be called when ADB Reboot is pressed
# This has to be outside because ADB Reboot does not require APK or JSON dependancy
# This should be enabled always
def reboot(event):

    # Create an instance for TestReplace class and call myadbreboot method
    t = TestReplace()
    t.myadbreboot(wx.EVT_BUTTON)


def testbrowse(event):

     """
     :param event:
     This method will be called whenever the browse button for JSON
     file is pressed. it will store the path in json_path dictionary
     """

     # Creates a wxPython file dialog
     browse_filedialog = wx.FileDialog(myframe,
                                       message = "Browse",
                                       defaultFile = "",
                                       wildcard = "*.json",
                                       style = wx.FD_OPEN)

     # If OK is pressed, store the path else return
     if browse_filedialog.ShowModal() == wx.ID_OK:
        mypaths["json_path"] = browse_filedialog.GetPath()
     else:
        return

     if mypaths["json_path"] != None:
         m = MyUI(mypaths["json_path"],mypaths["apk_path"])
         m.editors()
         Jsonpath.SetValue(mypaths["json_path"])
         return

def testapkbrowse(event):

     """
     :param event:
     This method will be called whenever the browse button for APK File
     file is pressed. it will store the path in apk_path dictionary
     """

     # Creates a wxPython file dialog
     browse1_filedialog = wx.FileDialog(myframe, message = "Browse",
                                          defaultDir = os.getcwd(),
                                          defaultFile = "",
                                          wildcard = "*.apk",
                                          style = wx.FD_OPEN)

     # If OK is pressed, store the path else return
     if browse1_filedialog.ShowModal() == wx.ID_OK:
        mypaths["apk_path"] = browse1_filedialog.GetPath()
     else:
        return


     if mypaths["apk_path"] != None:
         m = MyUI(mypaths["json_path"],mypaths["apk_path"])
         m.adboperation()
         Apkpath.SetValue(mypaths["apk_path"])
         return



class MyUI:
    """
     This class has all the UI components and their respective button actions bound.
     The methods which will be called as a result of action are available in my_replace.py
     file
    """


    def __init__(self,json_path,apk_path):

        self.json_path = json_path
        self.apk_path = apk_path



    def editors(self):

        # Create an instance for TestReplace class and pass both the paths
        t = TestReplace(self.json_path, self.apk_path)

        Prerollchange.Enable()
        Prerollchange.Bind(wx.EVT_BUTTON,t.myprerollreplace)


        Midrollchange.Enable()
        Midrollchange.Bind(wx.EVT_BUTTON,t.mymidrollreplace)

        Postrollchange.Enable()
        Postrollchange.Bind(wx.EVT_BUTTON,t.mypostrollreplace)

        Norollchange.Enable()
        Norollchange.Bind(wx.EVT_BUTTON,t.mynorollreplace)

        sethlsvodurlbipbop.Enable()
        sethlsvodurlbipbop.Bind(wx.EVT_BUTTON,t.myHLSVODbipbop)

        sethlsvodurlipad.Enable()
        sethlsvodurlipad.Bind(wx.EVT_BUTTON,t.myHLSVODipadakamai)

        sethlsvodurlqhttp.Enable()
        sethlsvodurlqhttp.Bind(wx.EVT_BUTTON,t.myHLSVODqhttp)

        sethlsliveurlbipbop.Enable()
        sethlsliveurlbipbop.Bind(wx.EVT_BUTTON,t.myHLSLIVEbipbop)

        sethlsliveurlvevo.Enable()
        sethlsliveurlvevo.Bind(wx.EVT_BUTTON,t.myHLSLIVEvevo)

        setssvodurlbb.Enable()
        setssvodurlbb.Bind(wx.EVT_BUTTON,t.mySSbigbunny)

        setssliveurlvevo.Enable()
        setssliveurlvevo.Bind(wx.EVT_BUTTON,t.mySSLIVE)

        setssliveurlslight.Enable()
        setssliveurlslight.Bind(wx.EVT_BUTTON,t.mySSLIVESlight)

        setmp4urllp.Enable()
        setmp4urllp.Bind(wx.EVT_BUTTON,t.myMP4livepass)

        setmp4urlen.Enable()
        setmp4urlen.Bind(wx.EVT_BUTTON,t.myMP4envato)

        togglegateway.Enable()
        togglegateway.Bind(wx.EVT_BUTTON,t.setbadgateway)

        resetgateway.Enable()
        resetgateway.Bind(wx.EVT_BUTTON,t.touchstonegateway)

        sethlsad.Enable()
        sethlsad.Bind(wx.EVT_BUTTON,t.myHLSad)

        setssad.Enable()
        setssad.Bind(wx.EVT_BUTTON,t.mySSad)

        setmp4ad.Enable()
        setmp4ad.Bind(wx.EVT_BUTTON,t.mymp4ad)

        setislivet.Enable()
        setislivet.Bind(wx.EVT_BUTTON,t.setislivetrue)

        setislivef.Enable()
        setislivef.Bind(wx.EVT_BUTTON,t.setislivefalse)

        adbpush.Enable()
        adbpush.Bind(wx.EVT_BUTTON,t.myadbpush)


    def adboperation(self):
        """
        This is required as a separate method because this has a dependancy on apk file. This should not
         be enabled if the JSON file is selected. However it should still work if only apk file is selected.
        """

        t = TestReplace(self.json_path, self.apk_path)

        adbinstall.Enable()
        adbinstall.Bind(wx.EVT_BUTTON,t.myadbinstall)


if __name__ == "__main__":

   app = wx.App()
   myframe = wx.Frame(None,
                       wx.BORDER_DEFAULT,
                       title = "JSON_EDITOR",
                       size = (450,500),
                       style = wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)


   Jsonpath = wx.TextCtrl(myframe,wx.BORDER_DEFAULT,pos = (15,3),size = (300,25))
   Jsonpath.SetValue("Please browse a JSON file to edit")
   Jsonpath.Disable()

   Apkpath = wx.TextCtrl(myframe,wx.BORDER_DEFAULT,pos = (15,35),size = (300,25))
   Apkpath.SetValue("Please browse an apk file to install")
   Apkpath.Disable()

   # Browse button to locate a json file and browse
   BrowseButton1 = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Browse",pos = (340,3))
   BrowseButton1.Bind(wx.EVT_BUTTON, testbrowse)

   BrowseButton2 = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Browse",pos = (340,35))
   BrowseButton2.Bind(wx.EVT_BUTTON, testapkbrowse)

   Prerollchange = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Enable Preroll",pos = (20,80),size = (200,25))
   Prerollchange.Disable()



   Midrollchange = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Enable Midroll",pos = (20,110),
                             size = (200,25))
   Midrollchange.Disable()

   Postrollchange = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Enable Postroll",pos = (20,140), size = (200,25))
   Postrollchange.Disable()

   Norollchange = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Enable Noroll",pos = (20,170),size = (200,25))
   Norollchange.Disable()

   adbreboot = wx.Button(myframe,wx.BORDER_DEFAULT,label = "ADB Reboot",pos = (20,350),size = (200,25))
   adbreboot.Bind(wx.EVT_BUTTON,reboot)

   adbinstall = wx.Button(myframe,wx.BORDER_DEFAULT,label = "ADB Install",pos = (20,380), size = (200,25))
   adbinstall.Disable()

   sethlsvodurlbipbop = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set HLSVODURL_BIP BOP",pos = (225,80), size = (200,25))
   sethlsvodurlbipbop.Disable()

   sethlsvodurlipad = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set HLSVODURL_IPAD AKAMAI",pos = (225,110), size = (200,25))
   sethlsvodurlipad.Disable()

   sethlsvodurlqhttp = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set HLSVODURL_QHTTP",pos = (225,140), size = (200,25))
   sethlsvodurlqhttp.Disable()

   sethlsliveurlbipbop = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set HLSLIVEURL_BIP_BOP",pos = (225,170), size = (200,25))
   sethlsliveurlbipbop.Disable()

   sethlsliveurlvevo = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set HLSLIVEURL_VEVO",pos = (225,200), size = (200,25))
   sethlsliveurlvevo.Disable()

   setssvodurlbb = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set SSVODURL_BIGBUNNY",pos = (225,230), size = (200,25))
   setssvodurlbb.Disable()

   setssliveurlvevo = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set SSLIVEURL_VEVOPLAYLIST",pos = (225,260), size = (200,25))
   setssliveurlvevo.Disable()

   setssliveurlslight = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set SSLIVEURL_SILVERLIGHT",pos = (225,290), size = (200,25))
   setssliveurlslight.Disable()

   setmp4urllp = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set MP4URL LIVEPASS",pos = (225,320), size = (200,25))
   setmp4urllp.Disable()

   setmp4urlen = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set MP4URL ENVATO",pos = (225,350), size = (200,25))
   setmp4urlen.Disable()

   togglegateway = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set Bad GatewayURL",pos = (225,380), size = (200,25))
   togglegateway.Disable()

   resetgateway = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set Touchstone GatewayURL",pos = (225,410), size = (200,25))
   resetgateway.Disable()

   sethlsad = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set HLS AD URL",pos = (20,200),size = (200,25))
   sethlsad.Disable()

   setssad = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set SS AD URL",pos = (20,230),size = (200,25))
   setssad.Disable()

   setmp4ad = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set MP4 AD URL",pos = (20,260),size = (200,25))
   setmp4ad.Disable()

   adbpush = wx.Button(myframe,wx.BORDER_DEFAULT,label = "ADB Push",pos = (20,410), size = (200,25))
   adbpush.Disable()

   setislivet = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set isLive True",pos = (20,290),size = (200,25))
   setislivet.Disable()

   setislivef = wx.Button(myframe,wx.BORDER_DEFAULT,label = "Set isLive False",pos = (20,320),size = (200,25))
   setislivef.Disable()

   myframe.Show()
   app.MainLoop()


