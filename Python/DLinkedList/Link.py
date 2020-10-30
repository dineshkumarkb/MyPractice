class Link(object):

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self,nnext):
        self.next = nnext

    def set_prev(self,pprev):
        self.prev = pprev

    def get_data(self):
        return self.data

    def display_list(self):
        print " The list element is : ", self.data