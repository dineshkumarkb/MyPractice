class MyDict(dict):
    """
    This class inherits Python's standard class dictionary
    and adds few extra implementations
    """

    def __init__(self):
        dict.__init__(self)
        self.mydict = {}

    def __setitem__(self, key, value):

        self.mydict[key] = value

    def __getitem__(self, item):

        return self.mydict[item]

    def dicttolistsort(self,dicttosort):
        """
        :param dicttosort:
        :return:
         This method takes a dictionary as a parameter and sorts all the keys and returns
         the sorted key value pairs
        """
        try:
            assert isinstance(dicttosort,dict)
        except: AssertionError,TypeError,AttributeError

        l = []
        mykeys = dicttosort.keys()
        mykeys.sort()
        for keys in mykeys:
            l.append(keys)
            l.append(dicttosort[keys])

        return l

    def returnkeys(self):

        return self.mydict.keys()

    def values(self):
        """
        This method will return  a list of sorted values
        :return: sorted list of values
        """

        return self.mydict.values()


if __name__ == "__main__":
    m = MyDict()
    m["INTEGRATION_ID"] = "integrationId"
    d = {"INTEGRATION_ID" : "integrationId","DRIVER_REQUEST_INTERVAL_SEC" : 2.55, "PLAYER_READY_DELAY_MS": "test"}
    l = []
    print m.dicttolistsort(l)



