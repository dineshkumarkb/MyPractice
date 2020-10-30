def check_even(func):
    def wrapper(*args):
        number = args[1]
        if(number % 2 == 0):
            return func(*args)
        else:
            print " Number is not even "
            return
    return wrapper








class CheckEven(object):

    def __init__(self):
        self.even_list = []


    @check_even
    def make_evenlist(self,number):
        self.even_list.append(number)
        print " The list is ",self.even_list





c = CheckEven()
c.make_evenlist(3)