# Author : DineshKumar
# Date Modified : 22-07-2016
# This is to automate the build for any js based player and copy into the build folder

from subprocess import Popen,PIPE
import sys

class JsBuildAuto:

    ''' All the player make commands and copy commands have been stored in a class variable dictionary'''

    top_level_build_folder_path = r'build/js-cws'
    dest_build_folder_path = r'sdk/js'

    playerconfig = {0: {"JWPLAYER" : r'make jwplayer_cws_clean jwplayer_cws'},
                    1: {"VIDEO_JS" : r'make videojs_cws_clean videojs_cws'},
                    2: {"CHROMECAST" : r'make chromecast_cws_clean chromecast_cws'},
                    3: {"HTML5" : r'make html5_cws'},
                    4: {"PRIMETIME" : r'make primetime_flash_cws primetime_flash_cws_clean'}}

    copyconfig = {0: r'cp -R build/js-cws/jwplayer sdk/js/build',
                  1: r'cp -R build/js-cws/videojs sdk/js/build',
                  2: r'cp -R build/js-cws/chromecast sdk/js/build',
                  3: r'cp -R build/js-cws/html5 sdk/js/build',
                  4: r'cp -R build/flash-cws/flex-debug sdk/js/build',
                  }


    def __init__(self):

        # A list to store the builds supported
        self.playerlist = ["JWPLAYER","VIDEO_JS","CHROMECAST","HTML5","PRIMETIME"]
        print "Please enter the respective number to start the build"

        for i,j in enumerate(self.playerlist):
            print "{}.{}".format(i,j)

        try:
            player = input("Please enter the player you wanna build: ")
            print "You have selected {}".format(self.playerlist[player])

        except KeyboardInterrupt:
            print "Interrupted"
            sys.exit(0)

        except Exception as e:
            print e, "Please enter a valid number"
            sys.exit(0)

        # Call the respective make commands as per the selected player
        build_command = self.selectPlayer(player)
        self.startbuild(build_command,player)


    def selectPlayer(self,player):

        '''This is the code to return the class variables based on the user input'''

        return JsBuildAuto.playerconfig[player][self.playerlist[player]]


    def startbuild(self,build_cmd,player):
        ''' This method will enter the build commands corresponding to the player
        @param : build_cmd --  The build command from playerconfig returned by select player method
        @param : player -- The integer input from the user'''

        # Store the cpy command for the respective player
        copyPlayer = JsBuildAuto.copyconfig[player]

        p = Popen(build_cmd, shell = True, stderr = PIPE, stdout = PIPE)

        # This line is mandatory to wait for the build to completed. Commnunicate will wait till the Popen command's
        # action is complete
        a = p.communicate()

        # Check for Errors if any
        if (("error" or "Error") in str(a) or
            "not recognized" in str(a) or
            "No rule" in str(a)):
            print "Error while building"
            print str(a)
        else:
            print "Build success"
            self.copyresults(copyPlayer)

    def copyresults(self, copycmd):
        '''
        This method will be called after the build command and the folder from devicesfringe/build wll be copied
        to sdk/js
        @param copycmd:
        @return: None
        '''

        p = Popen(copycmd, shell=True, stdout=PIPE, stderr=PIPE)
        # This line is mandatory to wait for the copy action to completed. Commnunicate will wait till the Popen command's
        # action is complete
        p.communicate()
        if p.returncode == 1:
            print "copy failed"
        else:
            print "Copy Success"


if __name__ == "__main__":

    j = JsBuildAuto()
