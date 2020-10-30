class StringTest:

    def __init__(self, s1, s2):

        self.s1 = s1
        self.s2 = s2

    def getS1(self):

        return self.s1

    def getS2(self):

        return self.s2

    def __str__(self):

        return self.s1 + " " +  self.s2





s = StringTest("Dinesh","Kumar")
print s