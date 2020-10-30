class MySingleton:

    instance = None

    def __init__(self):

        if self.instance is not None:
            raise ValueError("An instance already exists")


    @classmethod
    def getInstance(cls):

        if cls.instance is None:
            cls.instance = MySingleton()
        return cls.instance

    def printme(self):

        print "This is an example of a Singleton"



test = MySingleton.getInstance()
test.printme()