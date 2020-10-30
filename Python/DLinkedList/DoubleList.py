from Link import Link

class DoubleList(object):

    def __init__(self):

        self.first = None
        self.last = None

    def insert_first(self,data):
        link = Link(data)
        current = self.first

        if(current is None):
            self.last = link

        else:
            current.set_prev(link)
        self.first = link
        self.first.set_next(current)

    def insert_last(self,data):
        link = Link(data)
        current = self.last
        if(current is None):
            self.first = link
        else:
            current.set_next(link)
            link.set_prev(current)

        self.last = link

    def delete_first(self):

        current = self.first

        if(current is None):
            raise Exception, " List is null "

        self.first = self.first.get_next()
        self.first.set_prev(None)

        print " The deleted element is : ", current.get_data()

    def delete_last(self):

        current = self.last

        if(current is None):
            raise Exception, " List is null "

        self.last = self.last.get_prev()
        self.last.set_next(None)

        print " The deleted element is : ", current.get_data()


    def insert_after(self,key,data):
        link =  Link(data)
        current = self.first
        prev = None

        if (current is None):
            raise Exception, " List is null "




        while(current is not None):
            if(current.get_data() != key):
                prev = current
                current = current.get_next()
            else:
                break

        if (current == self.last):
            self.last = link
            self.last.set_next(None)

        else:
            current.get_next().set_prev(link)
            link.set_next(current.get_next())
        link.set_prev(current)
        current.set_next(link)


    def print_list_forward(self):
        current = self.first
        while(current != None):
            current.display_list()
            current = current.get_next()

    def print_list_backward(self):
        current = self.last
        while(current != None):
            current.display_list()
            current = current.get_prev()


if __name__ == "__main__":
    d = DoubleList()
    d.insert_first(10)
    d.insert_first(20)

    d.insert_last(40)
    d.insert_last(50)

    d.insert_after(50,45)

    #d.delete_last()

    d.print_list_forward()

    print " "

    d.print_list_backward()







