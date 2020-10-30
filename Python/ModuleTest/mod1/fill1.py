from ModuleTest.mod2 import fill2

def call_fill1():
    print("Printed from mod1 fill1")
    fill2.call_fill2()

call_fill1()