#!/usr/bin/env python

try:
    from jira import JIRA, JIRAError
except Exception as e :
    print " JIRA module not found in system"
    print " Installing ..."
    import pip
    pip.main(['install','jira'])

import socket
import argparse
import getpass
import sys


class JiraUtil(object):

    # The below two variables should be in class level and do not change these in instances
    jira_url = r'jira.corp.conviva.com'
    commandlist =  ["add_watcher",
                    "remove_watcher",
                    "add_comment",
                    "create_issue",
                    "addIssuesToEpic",
                    "addIssuesToSprint",
                    "attachfiles",
                    "assignIssues"]

    def __init__(self, username = None, password = None):

        self.username = username
        self.password = password

        if((self.username == None) or (self.password == None) or (self.password == "")):
            print " UserName/Password cannnot be None "
            return

        else:
            self.checkNetworkConnectivity()

    def checkNetworkConnectivity(self):

        """ Method to check the network connectivity of the local machine to the JIRA server """

        try:
            # For this check, http should not be prefixed. Hence the url doesnt have one
            socket.create_connection((JiraUtil.jira_url,80))
            self.startJIRA()

        except JIRAError as e:
            # All JIRA errors will be caught at this level
            print " JIRA connectivity failed : ", e.response
            return

        except KeyboardInterrupt:
            # Handling Ctrl+c and any keyboard interrupts
            print " Exiting ..."
            sys.exit(0)

    def startJIRA(self):
        """ This is the main method where the execution starts after we are able to connect to JIRA.
            We should have the credentials when we hit this method after which we login to JIRA using
            the same. This will display all the available commands to the user and allow them to select
            one of their choice.
        """

        # Login to the jira URL. The URL has to prefixed with http://. Else this will throw an error.
        # The below line is mandatory to log into JIRA
        JiraUtil.jira_url = r'http://'+ JiraUtil.jira_url
        self.jira = JIRA(JiraUtil.jira_url, basic_auth=(self.username,self.password))
        for i,j in enumerate(JiraUtil.commandlist):
            print " {}.{} ".format(i+1,j)
        self.action = raw_input(" Syntax: \n "
                                " command_number [tickets list separated by commas] [usernames separated by commas excluding self] \n ")
        try:
            self.commandlines = self.action.split(" ")
            self.ticketsList = self.commandlines[1]
            # This is to ensure we will handle usernames other than self
            if(len(self.commandlines) > 2):
                # Multiple usernames will be used only for
                # Add/Remove watchers mostly
                 local_username = self.action.split(" ")[2]
            else:
                # When no username is given, we take the default username which is logged in
                local_username = self.username
            if(len(self.ticketsList) > 1):
                # Here the ticketsList will always be of type list
                # Scenario for delimiter not found need not be handled as all methods
                # will iterate through the list and do the needful
                self.ticketsList = self.ticketsList.split(",")
        # Index error should be caught if user does not provide any JIRA ID
        # self.action.split(" ") will throw index error.
        except IndexError as e:
            print " Please provide atleast one JIRA ID ", e.message
            self.startJIRA()
        # Parse user actions based on the values provided and call the respective methods
        if (self.action[0] == str(1)):
           self.addRemoveWatcher("add", username = local_username,ticketList = self.ticketsList)
        elif (self.action[0] == str(2)):
           self.addRemoveWatcher("remove", username = local_username, ticketList = self.ticketsList)
        elif (self.action[0] == str(3)):
            self.addComment(self.ticketsList)
        elif (self.action[0] == str(4)):
            print " Function Not Available. Please select other options "
            self.startJIRA()
        elif (self.action[0] == str(5)):
            epic_id = raw_input(" Please enter the epic id : ")
            if((epic_id != None) and (epic_id != "")):
                self.addIssuestoEpic(epic_id,ticketsList = self.ticketsList)
            else:
                print " Epic ID cannot be blank or null "
                ''' We are calling this function recursively. Since we dont rely on the state of any variables
                 this should be safe '''
                self.startJIRA()
        elif (self.action[0] == str(6)):
            pass
        elif (self.action[0] == str(7)):
            self.filepath = raw_input(" Please provide a file path : ")
            if(self.filepath == None or self.filepath == ""):
                print " Please enter a file path "
                ''' We are calling this function recursively. Since we dont rely on the state of any variables
                this should be safe '''
                self.startJIRA()
            self.attachFiles(self.ticketsList,self.filepath)
        elif (self.action[0] == str(8)):
            self.assignee = raw_input(" Please provide an assginee name : ")
            if (self.assignee == None or self.assignee == ""):
                print " Please enter an assignee name :  "
                ''' We are calling this function recursively. Since we dont rely on the state of any variables
                    this should be safe '''
                self.startJIRA()
            self.assignIssues(self.ticketsList,self.assignee)


    def addComment(self, ticketList = None):
        """ Method to add comments to the JIRA tickets
            :param ticketList : List of the tickets in which the comment has to be added      
        """
        comment = raw_input(" Enter Comment : ")
        for ticket in ticketList:
            self.jira.add_comment(ticket,comment)

    def addIssuestoEpic(self, epic_id = None, ticketsList = None):
        """ 
        :param epic_id: The jira id of epic tickey
        :param ticketsList: list of the JIRAs to be added
        :return: None
        We have to pass the list of issues to the add_issues_to_epic() method. Hence we dont 
        iterate through the list and pass single tickets like we do for other methods
        """
        self.jira.add_issues_to_epic(epic_id, ticketsList)

    def attachFiles(self, jira_id, path):
        """ This method attaches the files passed to the corresponding JIRA ticket
          :param jira_id : List of JIRA ID(s) to which the file is to be attached
          :param path : The absolute file path of the file to be uploaded        
        """
        try:
           # jira_id is a list. Hence we iterate and then add the files to the ticket
           for ticket in jira_id:
               self.jira.add_attachment(ticket, path)
        except IOError:
            print " Please check if the filename/path is valid "
            self.startJIRA()

    def assignIssues(self, ticketList = None, assignee = None):
        """ :param ticketList :  List of tickets to be assigned to a user
            :param assignee : assignee   """

        for ticket in ticketList:
            self.jira.assign_issue(ticket,assignee)


    def addRemoveWatcher(self, func_type, username = None, ticketList = None):

        """ Method to add/remove watchers to a single or list of JIRA tickets
            This is the only method where both the usernames and ticketlists can 
            be multiple values
            :param username : list of usernames
            :param ticketList :  list of tickets
        """

        if len(username) > 1:
            local_username = username.split(",")
        else:
            local_username = self.username

        if ticketList is not None:
            for ticket in ticketList:
                for users in local_username:
                    if func_type == "add":
                        self.jira.add_watcher(ticket,users)
                    elif func_type == "remove":
                        self.jira.remove_watcher(ticket,local_username)
        else:
            print " Please provide JIRA ticket numbers "


    def createIssue(self):

        self.jira.create_issue()


    def addIssuestoSprint(self):
        pass


class PasswordHide(argparse.Action):
    """ This piece of code is to hide the password from getting displayed on the command prompt
         getpass.getpass() will take care of this. The __call__ method will be called when user is prompted for a 
         password and stored in namespace variable """

    def __call__(self, parser, namespace,values, option_string):
        password =  getpass.getpass()
        setattr(namespace,self.dest,password)


if __name__ == "__main__":

    try:
        parser = argparse.ArgumentParser(description = "Create/Modify the JIRA contents from command line")
        parser.add_argument("username",help = " Enter your JIRA username ")
        parser.add_argument("password", action = PasswordHide,nargs = "?",help=" Enter your JIRA password ")
        args = parser.parse_args()
        j = JiraUtil(args.username, args.password)
        parser.add_argument("JIRA ID", nargs = "?", help = " Enter the JIRA ID you want to modify ")

    except KeyboardInterrupt:
        print "Application Interrupted"


