from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyLogin:

    def __init__(self):

        self.myurl = "http://touchstone.conviva.com"
        self.myuser = "dkumar@conviva.com"
        self.mypass ="Pa55w0rd"

    def mypagelogin(self):

        self.mybrowser = webdriver.Chrome()
        self.mybrowser.get(self.myurl)

    #def myseleniumwait(self,myelement):

    #    WebDriverWait(self.mybrowser,30).until(EC.presence_of_element_located(By.CLASS_NAME,myelement))

    def mycredentials(self):

        self.enter_user = self.mybrowser.find_element_by_id("loginBox")
        self.enter_user.send_keys(self.myuser)

        self.enter_pass = self.mybrowser.find_element_by_id("passwordBox")
        self.enter_pass.send_keys("Pa55w0rd")

        self.enter_submit = self.mybrowser.find_element_by_id("loginButton")
        self.enter_submit.send_keys(Keys.RETURN)
        self.mycurrenturl = self.mybrowser.current_url

        self.enter_LivepassTab = self.mybrowser.find_element_by_id("ui-id-4")
        self.enter_LivepassTab.send_keys(Keys.RETURN)

        self.starttouchstonebutton = self.mybrowser.find_element_by_id("startRemoteWithServiceUrlBtn")
        self.starttouchstonebutton.send_keys(Keys.RETURN)

        WebDriverWait(self.mybrowser,50).until(EC.presence_of_element_located((By.CLASS_NAME,"sourceTable")))

        self.mycount = 1

        for row in self.mybrowser.find_elements_by_xpath("//*[@id='clientsDiv']/table/tbody/tr/td[4]/div"):
            #myrows = row.find_elements_by_tag_name("td")[3]
            mytext = row.text
            print mytext
            #print self.mycount
            self.myxpath = "//*[@id='clientsDiv']/table/tbody/tr[{}]/td[7]/input".format(self.mycount)
            if mytext == "Unfinished Business":
                mybutton = row.find_element_by_xpath(self.myxpath)
                mybutton.click()
                break
            self.mycount+=1

    def expand_session(self):

        WebDriverWait(self.mybrowser,60).until(EC.presence_of_element_located((By.ID,"collapseSessionInfoButton")))
        collapse_button = self.mybrowser.find_element_by_id("collapseSessionInfoButton")
        collapse_button.click()


    def get_client_id(self):

        WebDriverWait(self.mybrowser,100).until(EC.presence_of_element_located((By.XPATH,"//*[@id='sessionInfoDiv']/div[1]/table/tbody/tr[3]/td[2]")))
        self.client_id = self.mybrowser.find_element_by_xpath("//*[@id='sessionInfoDiv']/div[1]/table/tbody/tr[3]/td[2]")
        print self.client_id.text
        return self.client_id.text

    def get_content_length(self):
        WebDriverWait(self.mybrowser,100).until(EC.presence_of_element_located((By.XPATH,".//*[@id='sessionInfoDiv']/div[4]/table/tbody/tr[6]/td[2]")))
        self.content_length = self.mybrowser.find_element_by_xpath(".//*[@id='sessionInfoDiv']/div[4]/table/tbody/tr[6]/td[2]")
        print self.content_length.text
        return self.content_length.text

    def get_viewer_id(self):
        WebDriverWait(self.mybrowser,100).until(EC.presence_of_element_located((By.XPATH,".//*[@id='sessionInfoDiv']/div[4]/table/tbody/tr[8]/td[2]")))
        self.viewer_id = self.mybrowser.find_element_by_xpath(".//*[@id='sessionInfoDiv']/div[4]/table/tbody/tr[8]/td[2]")
        print self.viewer_id.text
        return self.viewer_id.text

    def get_tagvalues(self):
        self.tag_values = self.mybrowser.find_element_by_xpath(".//*[@id='sessionInfoDiv']/div[1]/table/tbody/tr[6]/td[2]/textarea")
        print self.tag_values.text
        return self.tag_values.text



m = MyLogin()
m.mypagelogin()
m.mycredentials()
m.expand_session()
m.get_client_id()
m.get_content_length()
m.get_viewer_id()
m.get_tagvalues()

# X Path for text : html/body/pre/a[4]/text()
# X Path for HB 0 : .//*[@id='timelineTable']/div[2]/div[3]/div/a