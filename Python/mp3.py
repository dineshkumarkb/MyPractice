import os,sys
from UserDict import UserDict

def stripnulls(data):
    try:
        assert isinstance(data,str)
        return data.replace("\00","").strip()

    except (AssertionError,TypeError) as e:
        print " An Error occures",e


class FileInfo(UserDict):
    def __init__(self, filename = None):
        UserDict.__init__(self)
        self["name"] = filename

class MP3FileInfo(FileInfo):

    tagdatamap = {"title" : (3, 33, stripnulls),
                  "artist": (33, 63, stripnulls),
                  "album" : (63, 93, stripnulls),
                  "year" :  (93, 123, stripnulls),
                  "genre":  (123, 153, stripnulls)}


    def __parse(self,filename):

        self.clear()
        try:
            fsock = open(filename,"rb",0)
            try:
                fsock.seek(128,2)
                print"*****************", fsock.read(128)
                tagdata = fsock.read(128)
            finally:
                fsock.close()
            if tagdata[:3] == "TAG":
                for tag, (start, end, parseFunc) in self.tagdatamap.items():
                    self[tag] = parseFunc(tagdata[start:end])

        except IOError:
            pass

    def __setitem__(self, key, value):

        print "***************",item
        if key == "name" and item:
            self.__parse(item)
        FileInfo.__setitem__(self,key,item)


    def listDirectory(directory,fileExtList):

        print "Inside Listdirectory"

        fileList = [os.path.normcase(f) for f in os.listdir(directory)]
        fileList = [os.path.join(directory,f) for f in fileList if os.path.splitext(f)[1] in fileExtList]

        def getFileInfoClass(filename,module = sys.modules[FileInfo.__module__]):

            print "inside getfileinfoclass"

            subclass = "%s Fileinfo" % os.path.splitext(filename)[1].upper()[1:]
            return hasattr(module,subclass) and getattr(module,subclass) or FileInfo

        return [getFileInfoClass(f)(f) for f in fileList]

    if __name__ == "__main__":
        for info in listDirectory("D:\\Songs","[.mp3]"):
            print "\n".join(["%s = %s" %(k,v) for k,v in info.items()])






