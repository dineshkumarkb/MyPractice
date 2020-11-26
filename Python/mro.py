class A(object):

    def __init__(self):
        pass

    def display(self):
        print(f" From class A")


class B(A):

    def display(self):
        print(f" From class B")


class C(A):

    #pass

    def display(self):
        print(f" From C")


class D(C,B):

    #pass

    def display(self):
        print(f" From D")

D().display()



