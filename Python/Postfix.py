from MyStack import MyStack

class Postfix(object):

    def __init__(self,inp_string = None):
        try:
            if ((inp_string is not None) and (len(inp_string) > 0)):
                op_stack = MyStack(len(inp_string))
                self.inp_string = inp_string
                self.convert_postfix()
                self.out_string = None
            else:
                raise InvalidStringException

        except InvalidStringException as e:
            print " InvalidStringException "


    def convert_postfix(self):
        for s in self.inp_string:
            print s


class InvalidStringException(Exception):
    """  InvalidStringException """
    pass


if __name__ == "__main__":
    s = "A+B-C"
    p = Postfix(s)