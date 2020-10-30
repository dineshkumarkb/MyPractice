class CharCount(object):

    chardict = {}
    charArr = []

    def __init__(self, name):

        self.name = name
        if((self.name == None) or (self.name == "")):
            return
        self.storeInArray(self.name)


    def storeInArray(self, name):

        for chars in name:
            self.charArr.append(chars)
            self.chardict.setdefault(chars,0)
        self.calcLetters()

    def calcLetters(self):
        for chars in self.charArr:
            self.chardict[chars]+=1


if __name__ == "__main__":
    myname = raw_input(" Please enter a name : ")
    CharCount(myname)
