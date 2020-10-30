class Func_Prop(object):


    def __init__(self):
        pass


    def func1(self, amount):
        self.amount = amount


    def func2(self,title,author):
        self.title = title
        self.author = author
        self.callme = self.func1



f = Func_Prop()
f.func2("Inferno","Dan brown")
f.callme(100)

print f.title
print f.author




