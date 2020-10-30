from engine.testCase import *
import engine.TestConfiguration as C
import time

@testclass(capabilities=[C.CWS_CLIENT])

class TestSanity(TestCase): 
    def __init__(self):
     
         TestCase.__init__(self)
     
    @testmethod()     
    def testsanitycontentlength(self):
        """ This test case validates the content length of the video during playback"""
        
        # Initialize the session
        CwsSession.cwsInit(self)
        
        # Create a player instance and pass the URL
        player = Player(self,self.testConfig[C.STREAM_URL])
        session = CwsSession(self, player)
        self.waitUntilCurrentActionsSent()
        
        # Start the playback
        player.play()
        self.waitUntilCurrentActionsSent()
        self.waitSessionUntilTrue(lambda : session.ss.isPLAYING(), 15, desc = "Playback starts")

        # Adding this delay as few players crash on immediate actions
        self.waitSeconds(5,desc = "Wait for few seconds of playback")
        self.waitUntilCurrentActionsSent()
        
        # Compare the content length of the video
        AssertAreEqual(self.testConfig[C.STREAM_META_CONTENT_LEN_SEC], session.ss.contentLengthSec)
        self.log("The content length of the video is: %d" % session.ss.contentLengthSec)
        
        # Clean up the session and exit
        #CwsSession.cwsCleanup(self)
        self.log("End of testsanitycontentlength")


    @testmethod()
    def testsanityjointime(self):
        """This is to verify the test join time of the video"""

        # Initialize the session
        CwsSession.cwsInit(self)
        
        # Create a player instance and pass the URL
        player = Player(self,self.testConfig[C.STREAM_URL])
        session = CwsSession(self, player)
        self.waitUntilCurrentActionsSent()

        # Start the playback
        player.play()
        self.waitUntilCurrentActionsSent()
        self.waitSessionUntilTrue(lambda : session.ss.isPLAYING(), 15, desc = "Playback starts")

        # Adding this delay as few players crash on immediate actions
        self.waitSeconds(3,desc = "Wait for few seconds of playback")
        self.waitUntilCurrentActionsSent()

        # Compare the join time of the video
        AssertIsGeq(0, session.ss.joinTimeMs)
        self.log("The join time of the video is: %d" % session.ss.joinTimeMs)

        # Clean up the session and exit
        CwsSession.cwsCleanup(self)
        self.log("End of testsanitycontentlength")

    @testmethod()
    def testsanitybuffering(self):
        """This is to verify the buffering state of the video"""

        # Initialize the session
        CwsSession.cwsInit(self)

        # Check the network scheme and port no for the stream URL
        proxy = self.startVideoProxyForUrl(self.testConfig[C.STREAM_URL])

        params = self.testConfig[C.STREAM_BUFFERING_PARAMS]

        proxy.setInstructions([VideoProxy.ThrottleInstruction(capBytes = params['bytes_to_join']),VideoProxy.ThrottleInstruction(rateBps=params['Bps_to_buffer_1'])])

        # Create a player instance and pass the URL to the proxy
        player = Player(self, proxy.proxyUrl(self.testConfig[C.STREAM_URL]))

        # Create a cws session and pass the player instance
        session = CwsSession(self, player)
        player.play()
        self.waitUntilCurrentActionsSent()
        self.waitUntilTrue(lambda : session.ss.isReady() and session.ss.hasJoined(),
                           params['sec_wait_join'], 0.5,
                           desc="video join")

        # Check the buffering status
        self.waitUntilTrue(lambda : session.ss.isBUFFERING(), params['sec_wait_buffer_1'], 0.5,
                           desc="buffering after join")
        AssertAreEqual(1, session.ss.totalBufferingEvents)
        AssertIsGeq(1, session.ss.totalBufferingTimeMs)
        self.log("The buffering time of the video in ms is: %d" % session.ss.totalBufferingTimeMs)
        
        # Clean up the session and exit
        CwsSession.cwsCleanup(self)
        self.log("End of testsanitybuffering")

    @testmethod()
    def testsanityvsf(self):
        """ This test case is to verify basic video start failure error"""

        # Initialize the session
        CwsSession.cwsInit(self)

        # Create a player instance and pass the corrupt manifest URL to simulate VSF
        player = Player(self,self.testConfig[C.STREAM_URL_ALL_CHUNKS_MISSING])
        session = CwsSession(self, player)
        player.play()
        self.waitUntilCurrentActionsSent()
        self.waitSeconds(15,desc = "Wait for fatal error")
        self.waitUntilTrue(lambda : session.ss.isReady() and len(session.ss.fatalErrorEvents()) > 0,0.5,desc="Fatal Error event received")

        # Cleanup the session and exit
        CwsSession.cwsCleanup(self)
        self.log("End of testsanityvsf")

    @testmethod()
    def testsanitypreroll(self):
        """ This script is to test the preroll and join time after the preroll"""

        # Initialize the session
        CwsSession.cwsInit(self)

        # Create a player instance and start the video for preroll
        player = Player(self,self.testConfig[C.STREAM_URL])
        session = CwsSession(self, player)
        session.detachStreamer()
        player.play()
        self.waitSessionUntilTrue(lambda : session.ss.isNOT_MONITORED(), 15, desc = "Playback starts in not monitored state")
        self.waitUntilCurrentActionsSent()
        self.log("Player is in not monitored state")
        self.waitSeconds(15,desc = "Wait for ad playback to complete")
        
        # Start the playback of the main video
        session.attachStreamer(player)
        self.waitUntilCurrentActionsSent()
        self.waitSessionUntilTrue(lambda : session.ss.isPLAYING(), 15, desc = "Playback starts")
        
        # Cleanup the session and exit
        CwsSession.cwsCleanup(self)
        self.log("End of testsanitypreroll")


    @testmethod()
    def testpausetenmins(self):
        """ This test script is to verify that the player reports pause state for prolonged time"""

        # Initialize the session
        CwsSession.cwsInit(self)

        # Create a player instance and start the playback
        player = Player(self,self.testConfig[C.STREAM_URL])
        session = CwsSession(self, player)
        player.play()
        self.waitSessionUntilTrue(lambda : session.ss.isPLAYING(), 15, desc = "Playback starts")

        # Pause the player and check the play state
        player.pause()
        self.waitUntilCurrentActionsSent()
        self.waitSessionUntilTrue(lambda : session.ss.isPAUSED(), 15, desc = "Playback starts")

        # Wait for 5 minutes
        self.waitSeconds(300, desc = "Wait for 5 minutes in Pause state")

        # Check the state before exit
        if session.ss.isPAUSED():
            self.log("Pause state is maintained for 5 minutes")
            self.waitUntilCurrentActionsSent()

        # Cleanup the session
        CwsSession.cwsCleanup(self)

    """

    @testmethod()
    def testssbitrates(self):
        ''' This script is to validate the summation of audio and video bitrates for smooth streaming'''

        # Initialize the session
        CwsSession.cwsInit(self)

        # Create a player instance and start the playback
        player = Player(self,self.testConfig[C.STREAM_URL])
        session = CwsSession(self, player)
        player.play()
        self.waitSessionUntilTrue(lambda : session.ss.isPLAYING(), 15, desc = "Playback starts")

        # Get the current bitrate value and check if the same is the sum of audio and video bitrates
        currentbitratevalue = session.ss.currentBitrateKbps
        AssertIsIn(self.testConfig[C.STREAM_BITRATE_SUM],currentbitratevalue,"Compare the bitrate sum")

        # Cleanup the session
        CwsSession.cwsCleanup(self)


        @testmethod(disabledByIntegration=['Roku.*', "Ooyala.*"])
    def testPauseDuringBuffering_1(self):

        Check that we detect pauses even when currently buffering.
        Bugzilla Id : 4036.
        Steps:
        1.Play a video
        2.Throttle to a very low value for prolonged buffering.
        3.Pause the video and check the pause state.
        4.Again when we play the video the player should still be in buffering state as we have throttled.

        if self.testConfig[C.INTEGRATION_ID] == "Html5Touchstone.wk.1":
            assert False, "This test does not work on Chrome or Safari; use Firefox"

        # Initiate a cws session for current test
        CwsSession.cwsInit(self)

        # Creating a proxy connection between player and stream url, so that it can be throttled for testing purposes
        proxy = self.startVideoProxyForUrl(self.testConfig[C.STREAM_URL])

        # Creating a player with proxyUrl for throttling purposes
        player = Player(self, proxy.proxyUrl(self.testConfig[C.STREAM_URL]))
        session = CwsSession(self, player)
        player.play()

        # Check for the playing state
        self.waitUntilTrue(lambda : session.ss.isPLAYING(),10,desc="Check for playing state")

        # Throttle to a lower bitrate value to see Buffering for a prolonged duration so that the playback can be paused
        # during buffering
        proxy.setInstructions([VideoProxy.ThrottleInstruction(rateBps=self.testConfig[C.EBVS_THROTTLE_RATE_BPS])])

        # Wait for the buffering state to be displayed.
        self.waitUntilTrue(lambda : session.ss.isBUFFERING(),15,desc="Check for buffering state")

        # While buffering,pause the Video and wait for the pause state to be reported
        player.pause()
        self.waitUntilTrue(lambda : session.ss.isPAUSED(), 15, 0.5,desc="paused state detected")
        AssertAreEqual(True,session.ss.isPAUSED(),"Report Pause state")

        # Playback the video to check the buffering state as it is throttled
        player.play()
        self.waitUntilTrue(lambda : session.ss.isBUFFERING(), 15, 0.5,desc="paused state detected")

        # Assert for the total pause and buffering time
        AssertIsGeq(0, session.ss.totalPausedTimeMs)
        AssertIsGeq(0,session.ss.totalBufferingTimeMs)

        # Clean up the session
        CwsSession.cwsCleanup(self)






    @testmethod()
    def testseekend(self):
       #  This test script is to test seek forward and seek backward

        # Initializing the variable for seek
        seekOffsetMs = self.testConfig[C.STREAM_META_CONTENT_LEN_SEC] * 1000/5

        # Initialize the session
        CwsSession.cwsInit(self)

        # Create a player instance and start the playback
        player = Player(self,self.testConfig[C.STREAM_URL])
        session = CwsSession(self, player)
        player.play()
        self.waitSessionUntilTrue(lambda : session.ss.isPLAYING(), 15, desc = "Playback starts")
        self.waitUntilCurrentActionsSent()
        previousTotalPlayingTimeMs = session.ss.totalPlayingTimeMs
        print "*********************************", previousTotalPlayingTimeMs

        # Seeking the content forward
        player.seek(seekOffsetMs)

        # Wait for the playback to start again
        self.waitSessionUntilTrue(lambda : session.ss.isPLAYING(), 15, desc = "Playback resumes after seek")
        currentTotalPlayingTimeMs = session.ss.totalPlayingTimeMs
        print "*********************************", currentTotalPlayingTimeMs
        AssertIsGeq(currentTotalPlayingTimeMs,previousTotalPlayingTimeMs)

        # Clean up the session
        CwsSession.cwsCleanup(self)



    @testmethod()
    def vsfchunksunavailableOneStream(self):
        '''
         This script is to validate the vsf error when all the chunks of an url are unavailable
        '''
        # Initialize the session
        CwsSession.cwsInit(self)

        # Create a player instance and start the playback
        player = Player(self,self.testConfig[C.STREAM_URL_ONE_CHUNK_MISSING])
        session = CwsSession(self, player)
        player.play()

        self.waitUntilCurrentActionsSent()
        self.waitUntilTrue(lambda : session.ss.isPLAYING(),0.5,desc="Video playback starts")
        self.waitSeconds(60,desc = "Wait for playback")
        # Cleanup the session
        #CwsSession.cwsCleanup(self)





def playerStateChangeEvents(self):
        """
        Return the player state change events in this session
        @return:
        """
        print "**********************cwsEvents",self.cwsEvents
        for e in self.cwsEvents:
            print "********************************", e['t']
        return [e for e in self.cwsEvents if e['t'] == "CwsPlaystateChangeEvent"]
        
        

"""
    

        
        

   
