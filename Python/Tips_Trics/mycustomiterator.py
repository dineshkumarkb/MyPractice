class CustomIterator:

    def __init__(self, cust_object):
        """
        :param cust_object:
        """
        self.custom_object = cust_object
        self.max_len = len(cust_object)
        # print(f" The length of the object is {self.max_len} ")

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        if self.start < self.max_len:
            ret_value = self.custom_object[self.start]
            self.start += 1
            return  ret_value
        raise StopIteration


for i in CustomIterator({"name":"value"}):
    print(i)

