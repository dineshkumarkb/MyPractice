class Test(object):
    """
    This is a test class to ensure sphinx works fine
    """

    def __init__(self,my_str):
        """
        This is the constructor method with one arg for
        test class
        :param my_str:
        """
        self.my_str = my_str


    def get_var(self):
        """
        This is a getter method to return my_str variable
        :return:
        """

        return self.my_str