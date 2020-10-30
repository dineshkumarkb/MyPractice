class Listener:

    def __init__(self,source):
        source.registerListener(self)

    def notify(self,mysourceclass,*args,**kwargs):
        print "Got {} {} from class {}".format(args,kwargs,mysourceclass)


class Implementor1:

    def __init__(self):
        self.listeners = []

    def registerListener(self,className):
        self.listeners.append(className)

    def notifyListener(self,*args,**kwargs):
        for mylisteners in self.listeners:
            mylisteners.notify(self,args,kwargs)



class Listener2:

    def __init__(self,myobject):
        myobject.registerListener(self)

    def notify(self,sourceclass,*args,**kwargs):
        print "Got {} {} from {}".format(sourceclass,*args,**kwargs)




i = Implementor1()
l1 =  Listener2(i)
l = Listener(i)
i.notifyListener("Test")
