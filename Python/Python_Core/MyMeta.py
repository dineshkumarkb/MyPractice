class check_meta(type):
    print " Inside check_meta "

    def __new__(cls, clsname, bases,dct):
        ucase_attr = {}
        for k,v in dct.items():
            if not k.startswith('__'):
                ucase_attr[k.upper()] = v
            else:
                ucase_attr[k] = v

        return super(check_meta, cls).__new__(cls,clsname,bases,ucase_attr)



class TestMeta(object):

    __metaclass__ = check_meta

    test_field = "test"

    def func1(self):
        pass


print TestMeta().__class__.__dict__