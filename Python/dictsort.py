class sortme:

    def __init__(self,d = None):

        if d!= None:
            assert isinstance(d,dict)
        else:
            print "d is empty"

    def mysort(self,dic):
        """
        :param dic:
        :return: List with sorted key value pairs
        This method is to get a dictionary and return a list of sorted key value pairs
        for manipulation
        """
        mykeys = dic.keys()
        mykeys.sort()
        print "The sorted list of dictionaries are", mykeys
        return [("%s:%s") % (v,dic[v]) for v in mykeys]



if __name__ == "__main__":
    m = sortme()
    d = {"Name":"Dinesh","Place":"Bangalore","Zipcode": 560017}
    print m.mysort(d)

