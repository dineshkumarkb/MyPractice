class Node(object):
    """
    This class creates node objects for linked lists
    A node requires a next value and a data value
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    """
    This class creates a linked list using node objects
    """

    def __init__(self, head=None):
        self.head = head
        self.clone_head = None

    def insert_node(self, data):

        if not data:
            return

        node = Node(data)
        node.next = self.head
        self.head = node

    def clone_list(self, ll=None):
        """
        :param ll: A linked list object
        :return:
        """
        if not ll:
            return

        curr = self.head
        clone_ = LinkedList()

        while curr is not None:
            clone_.insert_node(curr.data)
            curr = curr.next

        clone_.display_lst()
        print(self.is_palindrome(ll, clone_ ))


    def display_lst(self, is_clone=False):

        if is_clone:
            curr = self.clone_head
        else:
            curr = self.head

        while curr:
            print(curr.data, end="->")
            curr = curr.next

    def is_palindrome(self, l1, l2):
        """
        :param l1:
        :param l2:
        :return:
        """

        if l1 is None or l2 is None:
            return False

        data1 = l1.head
        data2 = l2.head

        while data1 and data2:
            if data1.data != data2.data:
                return False
            data1 = data1.next
            data2 = data2.next

        return True


    def is_palindrome_list(self):

        lst_ = list()
        current = self.head

        while current:
            lst_.append(current.data)
            current = current.next

        if lst_ == lst_[::-1]:
            return True
        return False






l = LinkedList()
l.insert_node("0")
l.insert_node("1")
l.insert_node("2")
l.insert_node("1")
l.insert_node("0")
l.insert_node("5")
l.display_lst(False)
print()
l.clone_list(l)
print(l.is_palindrome_list())









