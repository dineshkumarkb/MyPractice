class Super(object):

    def __init__(self, name = None, age = None, lang = None):

        print(" The values are  {}, {}, {}").format(name,age,lang)

    def __new__(cls, *args, **kwargs):

        print (" Class Object ", cls)
        print (" Args ", args)
        print (" KW Args ", kwargs)

        return super(Super, cls).__new__(cls,*args,**kwargs)



Super("Dinesh", 30, lang = "python")